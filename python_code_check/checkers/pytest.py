import os
import subprocess
from datetime import datetime
import shutil
from pathlib import Path

from python_code_check.checkers.checker import Checker


class Pytest(Checker):

    NAME = "pytest"
    PATH_TO_AUTOTESTS = "../python_code_check/autotest_module/autotests/"

    _checks = {}

    def __init__(self, config_json, files_to_check):
        super().__init__(config_json, files_to_check)
        self._checks = config_json['checks']
        current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
        autotest_dir_name = f"{current_time}_test_pack/"
        self._path_to_current_autotest_pack = f"{self.PATH_TO_AUTOTESTS}{autotest_dir_name}"
        os.mkdir(self._path_to_current_autotest_pack)
        os.mkdir(f"{self._path_to_current_autotest_pack}/student_code/")

    def get_flags_from_configuration(self) -> []:
        pass

    @staticmethod
    def get_count_results_by_check_name(check_name, results):
        count = 0
        # for line in results:
        #     if line['type'] == check_name:
        #         count += 1
        return count

    def get_autotest_files_from_config(self):
        autotest_files = []
        for check in self._checks:
            autotest_files.append(check['test_file_path'])
        return autotest_files

    def get_autotest_files_from_current_tets_folder(self):
        from glob import glob
        glob_pattern = os.path.join(self._path_to_current_autotest_pack, "**", "*.py")
        autotest_files = []
        for file_path in glob(glob_pattern, recursive=True):
            autotest_files.append(file_path)
        return autotest_files

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

        self.copy_files_to_tests_folder()

        for autotest_path in self.get_autotest_files_from_current_tets_folder():
            result = subprocess.run(["pytest", autotest_path, "-v"], capture_output=True)
            output = result.stdout.decode("utf-8")
        #     check_json = {"checks": self.get_check_results(self._checks, result)}
        #     outcome = self.get_outcome([check_json["checks"]])
        #
        # current_time = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        # output_file_name = f"{current_time}_{self.NAME}.txt"
        # with open(f"outputs/{output_file_name}", "w", encoding="utf-8") as output_file:
        #     output_file.write(str(result.stderr))
        #     print(str(result.stderr))
        #
        # print("Pytest checked")

        return check_json, output_file_name, outcome

    def copy_files_to_tests_folder(self):
        for file_path in self._files_to_check:
            file_name = os.path.basename(file_path)
            shutil.copy(file_path, f"{self._path_to_current_autotest_pack}student_code/{file_name}")
        for file_path in self.get_autotest_files_from_config():
            file_name = os.path.basename(file_path)
            shutil.copy(file_path, f"{self._path_to_current_autotest_pack}{file_name}")
