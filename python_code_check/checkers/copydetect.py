import os

from python_code_check.checkers.checker import Checker
from shutil import which, copy, rmtree

class Copydetect(Checker):
    NAME = "copydetect"
    _check = []

    def __init__(self, config_json, files_to_check):
        super().__init__(config_json, files_to_check)
        self._check = config_json['check']

    def get_flags_from_configuration(self, check_name=None) -> []:
        pass

    def get_check_results(self, current_checks, extended_results) -> dict:
        pass

    def get_outcome(self, check_results: []) -> str:
        pass

    def start(self) -> tuple[dict, str, str]:
        if os.path.exists('test_directory'):
            rmtree('test_directory')

        os.mkdir('test_directory')
        for file in self._files_to_check:
            copy(file, 'test_directory')

        command = 'copydetect -t test_directory -r {} -a -d 0 --out-file \'output_copydetect\''.format(
            self._check['reference_directory'])
        os.system(command)
        rmtree('test_directory')

        self._check['check']['outcome'] = 'pass'
        self._check['check']['result'] = 0

        check_json = {'check': self._check['check']}

        full_output = "output_copydetect.html"
        outcome = 'pass'

        print('Copydetect checked')

        return check_json, full_output, outcome

