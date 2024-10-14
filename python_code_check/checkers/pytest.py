import os
import subprocess
from datetime import datetime

from python_code_check.checkers.checker import Checker


class Pytest(Checker):

    NAME = "pytest"
    PATH_TO_TESTS = "../Examples/TestExamples/hll_tests/tests/"
    PATH_TO_SRC = "../Examples/TestExamples/hll_tests/src/labs/"

    _check = {}

    def __init__(self, config_json, files_to_check):
        super().__init__(config_json, files_to_check)
        self._check = config_json['check']

    def get_flags_from_configuration(self) -> []:
        pass

    @staticmethod
    def get_count_results_by_check_name(check_name, results):
        count = 0
        # for line in results:
        #     if line['type'] == check_name:
        #         count += 1
        return count

    def get_check_results(self, current_check, results):
        if not current_check['enabled']:
            current_check['result'] = 0
            current_check['outcome'] = "skip"
        current_check['result'] = self.get_count_results_by_check_name(current_check, results)
        if current_check['result'] > current_check['limit']:
            current_check['outcome'] = "fail"
        else:
            current_check['outcome'] = "pass"
        return current_check

    def get_outcome(self, check_results):
        for result in check_results:
            if result['outcome'] == "fail":
                return "fail"
        return "pass"

    def start(self) -> tuple[dict, str, str]:

        self.load_files_to_tests_folder()
        path_to_test = f"{self.PATH_TO_TESTS}test_lab{self._config_json['check']['lab_number']}.py"
        result = subprocess.run(["pytest", "-v", path_to_test], capture_output=True)

        check_json = {"check": self.get_check_results(self._check, result)}
        outcome = self.get_outcome([check_json["check"]])

        current_time = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        output_file_name = f"{current_time}_{self.NAME}.txt"
        with open(f"outputs/{output_file_name}", "w", encoding="utf-8") as output_file:
            output_file.write(str(result.stderr))
            print(str(result.stderr))

        print("Pytest checked")

        return check_json, output_file_name, outcome

    def load_files_to_tests_folder(self):
        for file_path in self._files_to_check:
            file_name = os.path.basename(file_path)
            os.rename(file_path, f"{self.PATH_TO_SRC}lab_{self._config_json['check']['lab_number']}/{file_name}")
