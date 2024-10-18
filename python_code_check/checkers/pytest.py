import os
import re
import subprocess
from datetime import datetime
import shutil
from pathlib import Path

from python_code_check.checkers.checker import Checker


class Pytest(Checker):

    NAME = "pytest"
    PATH_TO_AUTOTESTS = "pytest_module/autotests/"

    _checks = {}
    _path_to_current_autotest_pack = ""
    _compair_path_to_tests = {}

    def __init__(self, config_json, files_to_check):
        super().__init__(config_json, files_to_check)
        self._checks = config_json['checks']
        current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
        autotest_dir_name = f"{current_time}_test_pack/"
        self._path_to_current_autotest_pack = f"{self.PATH_TO_AUTOTESTS}{autotest_dir_name}/"
        os.mkdir(self._path_to_current_autotest_pack)
        os.mkdir(f"{self._path_to_current_autotest_pack}student_code/")

    def get_flags_from_configuration(self, check_name=None) -> []:
        flags = ["-q"]
        if self.get_check_by_name(check_name)['autoreject']:
            flags.append("-x")
        return flags

    def get_count_results_by_check_name(self, extended_results):
        summary = re.search(r"\d.* failed, .* passed in .*(..*|.*)s", extended_results).group(0)
        failed = summary[0:summary.index(" failed,")]
        passed = summary[summary.index(" failed, ")+9:summary.index(" passed")]
        seconds = summary[summary.index("in ")+3:-1]
        return int(failed), int(passed), float(seconds)

    def get_autotest_from_config(self):
        autotest_files = {}
        for check in self._checks:
            if check['enabled']:
                autotest_files[check['check']] = check['test_file_path']
        return autotest_files

    def get_check_by_name(self, check_name):
        for check in self._checks:
            if check['check'] == check_name:
                return check
        return None

    def get_check_results(self, check, extended_results):
        if check is None:
            check = {'enabled': False}
        if not check['enabled']:
            check['result'] = 0
            check['outcome'] = "skip"
            return check
        check['failed'], check['passed'], check['seconds'] = self.get_count_results_by_check_name(extended_results)
        if check['failed'] > check['limit']:
            check['outcome'] = "fail"
        else:
            check['outcome'] = "pass"
        return check

    def get_outcome(self, check_results):
        for result in check_results:
            if result['outcome'] == "fail":
                return "fail"
        return "pass"

    def start(self) -> tuple[dict, str, str]:

        self.copy_files_to_tests_folder()

        checks_json = {"checks": []}
        total_output = ""
        for key, autotest_path in self._compair_path_to_tests.items():
            result = subprocess.run(["pytest"] + self.get_flags_from_configuration(key) + [autotest_path], capture_output=True)
            output = result.stdout.decode("utf-8")
            total_output += output + "\n\n"
            checks_json["checks"].append(self.get_check_results(self.get_check_by_name(key), output))

        outcome = self.get_outcome(checks_json["checks"])

        output_file_name = f"output.txt"
        with open(f"{self._path_to_current_autotest_pack}/{output_file_name}", "w", encoding="utf-8") as output_file:
            output_file.write(total_output)
            # print(total_output)

        print("Pytest checked")

        return checks_json, output_file_name, outcome

    def copy_files_to_tests_folder(self):
        for file_path in self._files_to_check:
            file_name = os.path.basename(file_path)
            shutil.copy(file_path, f"{self._path_to_current_autotest_pack}student_code/{file_name}")

        for key, autotest_file_path in self.get_autotest_from_config().items():
            file_name = os.path.basename(autotest_file_path)
            new_autotest_file_path = f"{self._path_to_current_autotest_pack}{file_name}"
            shutil.copy(autotest_file_path, new_autotest_file_path)
            self._compair_path_to_tests[key] = new_autotest_file_path

