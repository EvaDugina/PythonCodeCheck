from python_code_check.checkers.checker import Checker


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
        for file in files:
            copy(file, 'test_directory')

        command = 'copydetect -t test_directory -r {} -a -d 0 --out-file \'output_copydetect\''.format(
            data['tools']['copydetect']['check']['reference_directory'])
        system(command)
        rmtree('test_directory')
        data['tools']['copydetect']['full_output'] = "output_copydetect.html"
        data['tools']['copydetect']['outcome'] = 'pass'

        data['tools']['copydetect']['check']['outcome'] = 'pass'
        data['tools']['copydetect']['check']['result'] = 0

        print('Copydetect checked')

