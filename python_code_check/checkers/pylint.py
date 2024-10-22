import subprocess
from datetime import datetime
from pylint.reporters import JSONReporter
from pylint.lint import Run
from io import StringIO
import json
import os

from python_code_check.checkers.checker import Checker

class Pylint(Checker):

    NAME = "pylint"
    _checks = []

    # https://stackoverflow.com/questions/2028268/invoking-pylint-programmatically
    # https://sky.pro/wiki/python/otklyuchenie-preduprezhdeniy-pylint-reshenie-problemy-s-c0321/
    # https://docs.pylint.org/#command-line-options
    # https://dzen.ru/a/Yvs2SeunYGZ9Kv88

    def __init__(self, config_json, files_to_check):
        super().__init__(config_json, files_to_check)
        self._checks = config_json['checks']

    def get_flags_from_configuration(self, check_name=None):
        flags = []
        disable_checks = []
        for check in self._checks:
            if not check['enabled']:
                disable_checks.append(check['check'][0].upper())
            if 'disableErrorCodes' in check and len(check['disableErrorCodes']) > 0:
                for code in check['disableErrorCodes']:
                    disable_checks.append(code)
        if len(disable_checks) > 0:
            flags.append("--disable=" + ",".join(disable_checks))
        return flags

    @staticmethod
    def get_count_results_by_check_name(check_name, extended_results):
        count = 0
        for line in extended_results:
            if line['type'] == check_name:
                count += 1
        return count

    def get_check_results(self, current_checks, extended_results):
        for check in current_checks:
            if not check['enabled']:
                check['result'] = 0
                check['outcome'] = "skip"
                continue
            check['result'] = self.get_count_results_by_check_name(check['check'], extended_results)
            if check['result'] > check['limit']:
                check['outcome'] = "fail"
            else:
                check['outcome'] = "pass"
        return current_checks

    def get_outcome(self, check_results):
        for result in check_results:
            if result['outcome'] == "fail":
                return "fail"
        return "pass"

    def start(self) -> tuple[dict, str, str]:
        flags = self.get_flags_from_configuration()
        short_results = []
        extended_results = []
        non_parsed_output = ""

        # Проверять только те файлы, пути которых соответствуют определённым правилам
        # from glob import glob
        # glob_pattern = os.path.join(path, "**", "*.py")
        # for filepath in glob(glob_pattern, recursive=True):

        for filepath in self._files_to_check:
            reporter_buffer = StringIO()
            results = Run([filepath] + flags, reporter=JSONReporter(reporter_buffer), exit=False)
            score = results.linter.stats.global_note
            file_results = json.loads(reporter_buffer.getvalue())
            for element in file_results:
                non_parsed_output += f"{element['module']}.py:{element['line']}: {element['message-id']} ({element['symbol']}): {element['message']}\n"
            short_results.append({
                "filepath": os.path.realpath(filepath),
                "smell_count": len(file_results),
                "score": score
            })
            extended_results.extend(file_results)

        checks_json = {"checks": self.get_check_results(self._checks, extended_results)}
        outcome = self.get_outcome(checks_json["checks"])

        current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
        output_file_name = f"{current_time}_output_{self.NAME}.txt"
        with open(f"outputs/{output_file_name}", "w", encoding="utf-8") as output_file:
            output_file.write(non_parsed_output)
            # print(non_parsed_output)

        print("Pylint checked")

        return checks_json, output_file_name, outcome
