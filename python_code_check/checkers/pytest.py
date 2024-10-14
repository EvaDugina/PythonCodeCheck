

class Pytest:

    def __init__(self, config_json, files_to_check):
        super().__init__(config_json, files_to_check)
        self._checks = config_json['checks']

    def get_flags_from_configuration(self) -> []:
        pass

    def get_check_results(self, current_checks, extended_results) -> dict:
        pass

    def get_outcome(self, check_results) -> str:
        pass

    def start(self) -> tuple[str, dict, str]:
        pass
