
from datetime import datetime
from io import StringIO

from pylint.lint import Run
from pylint.reporters.text import TextReporter

from python_code_check.checkers.checker import Checker


class Pylint(Checker):

    _name = "pylint"

    # https://stackoverflow.com/questions/2028268/invoking-pylint-programmatically
    # https://sky.pro/wiki/python/otklyuchenie-preduprezhdeniy-pylint-reshenie-problemy-s-c0321/
    # https://docs.pylint.org/#command-line-options
    # https://dzen.ru/a/Yvs2SeunYGZ9Kv88

    def __init__(self, config_json, files_to_check):
        super().__init__(config_json, files_to_check)

    def get_args_from_configuration(self):
        return [] + self._files_to_check

    def get_outcome(self):
        return "pass"

    def start(self) -> tuple[str, dict, str]:
        pylint_args = self.get_args_from_configuration()
        pylint_output = StringIO()
        Run(pylint_args, reporter=TextReporter(pylint_output), exit=False)
        pylint_result = pylint_output.getvalue()

        for line in pylint_output.read():
            print(line)

        current_time = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        output_file_name = f"{current_time}_{self._name}.txt"
        with open(f"outputs/{output_file_name}", "w", encoding="utf-8") as output_file:
            output_file.write(pylint_result)

        work_status = "pass"
        work_output = {
            "full_output": output_file_name,
            "outcome": work_status
        }

        outcome = "pass"

        return "check", work_output, outcome

