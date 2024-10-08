import json
import unittest
import cProfile
from io import StringIO
from shutil import which

from pylint.lint import Run
from pylint.reporters.text import TextReporter

from python_code_check.checkers.flake8 import Flake8
from python_code_check.checkers.mypy import MyPy
from python_code_check.checkers.profiler import Profiler
from python_code_check.checkers.pyflakes import Pyflakes
from python_code_check.checkers.pylint import Pylint
from python_code_check.checkers.unuittests import UnitTests
from python_code_check.error import Result

CONFIGURATION_JSON = {}
FILES_TO_CHECK = []
OUTPUT_JSON = {}

TOOLS_COMPARISONS = {
    "pylint": Pylint,
    "pyflakes": Pyflakes,
    "flake8": Flake8,
    "mypy": MyPy,
    "unittests": UnitTests,
    "profiler": Profiler
}

def start(configuration) -> Result:
    global CONFIGURATION_JSON, FILES_TO_CHECK, OUTPUT_JSON
    with open(configuration["configuration_file_path"], encoding="utf-8") as configuration_file:
        CONFIGURATION_JSON = json.load(configuration_file)
    FILES_TO_CHECK = configuration['files_to_check']

    if not validate_configuration_json():
        return Result.ERROR_VALIDATE_CONFIGURATION_FILE
    OUTPUT_JSON = CONFIGURATION_JSON

    if not validate_files_to_check():
        return Result.ERROR_VALIDATE_FILES_TO_CHECK

    return run_tools()


def validate_configuration_json():
    if CONFIGURATION_JSON == {} or 'tools' not in CONFIGURATION_JSON:
        return False
    for key, tool in CONFIGURATION_JSON['tools'].items():
        if 'enabled' not in tool or 'show_to_student' not in tool:
            return False
        if 'bin' not in tool:
            continue
        if which(tool['bin']) is None:
            print("Tool " + tool['bin'] + " not installed, skipping..")
            tool['enabled'] = False
    return True


def validate_files_to_check():
    if len(FILES_TO_CHECK) < 1:
        return False
    return True


def run_tools():
    print("Running tools..")
    for key, tool in CONFIGURATION_JSON['tools'].items():
        checker = getCheckerByToolName(key)(tool, FILES_TO_CHECK)
        if checker is None:
            return Result
        if not checker.is_enabled():
            OUTPUT_JSON['tools'][key]['outcome'] = 'skip'
            continue
        result_tool_field, tool_result_json, outcome = checker.start()
        OUTPUT_JSON['tools'][key][result_tool_field] = tool_result_json
        OUTPUT_JSON['tools'][key]['outcome'] = outcome

    return Result.SUCCESS


def getCheckerByToolName(tool_name):
    if tool_name in TOOLS_COMPARISONS:
        return TOOLS_COMPARISONS[tool_name]
    return None



