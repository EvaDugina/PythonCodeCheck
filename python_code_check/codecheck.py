import json
from io import StringIO

from pylint.lint import Run
from pylint.reporters.text import TextReporter

from python_code_check.error import Result

CONFIGURATION_JSON = None
FILES_TO_CHECK = []


def start(configuration) -> Result:
    global CONFIGURATION_JSON, FILES_TO_CHECK
    with open(configuration["configuration_file_path"], encoding="utf-8") as configuration_file:
        CONFIGURATION_JSON = json.load(configuration_file)
    FILES_TO_CHECK = configuration['files_to_check']

    if not validate_configuration_json():
        return Result.ERROR_VALIDATE_CONFIGURATION_FILE

    if not validate_files_to_check():
        return Result.ERROR_VALIDATE_FILES_TO_CHECK

    check_code()
    return Result.SUCCESS


def validate_configuration_json():
    return True

def validate_files_to_check():
    return True


def check_code():
    run_pylint()


# https://stackoverflow.com/questions/2028268/invoking-pylint-programmatically
def run_pylint():
    pylint_args = get_pylint_args_from_configuration()
    pylint_output = StringIO()
    Run(pylint_args, reporter=TextReporter(pylint_output), exit=False)
    print(pylint_output.getvalue())
    for line in pylint_output.read():
        print(line)


def get_pylint_args_from_configuration():
    return [] + FILES_TO_CHECK
