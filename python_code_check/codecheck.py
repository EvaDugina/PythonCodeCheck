import json
from datetime import datetime
from shutil import which

from python_code_check.checkers.pytest import Pytest
from python_code_check.checkers.pylint import Pylint
from python_code_check.error import Result

CONFIGURATION_JSON = {}
FILES_TO_CHECK = []
OUTPUT_JSON = {}

TOOLS_COMPARISONS = {
    "pylint": Pylint,
    "pytest": Pytest,
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
        checker = getCheckerByToolName(key)
        if checker is None:
            OUTPUT_JSON['tools'][key]['outcome'] = 'skip'
            continue
        checker = checker(tool, FILES_TO_CHECK)
        if not checker.is_enabled():
            OUTPUT_JSON['tools'][key]['outcome'] = 'skip'
            continue
        checks_json, full_output, outcome = checker.start()
        OUTPUT_JSON['tools'][key].update(checks_json)
        OUTPUT_JSON['tools'][key]['full_output'] = full_output
        OUTPUT_JSON['tools'][key]['outcome'] = outcome

    save_output_json()

    return Result.SUCCESS


def save_output_json():
    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
    output_file_name = f"{current_time}_output.json"
    with open(f"outputs/{output_file_name}", "w", encoding="utf-8") as output_file:
        json.dump(OUTPUT_JSON, output_file, ensure_ascii=False, indent=4)


def getCheckerByToolName(tool_name):
    if tool_name in TOOLS_COMPARISONS:
        return TOOLS_COMPARISONS[tool_name]
    return None



