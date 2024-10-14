from python_code_check.checkers.checker import Checker


class Flake8(Checker):
    _name = "flake8"

    def __init__(self, config_json, files_to_check):
        super().__init__(config_json, files_to_check)

    def get_flags_from_configuration(self):
        return [] + self._files_to_check

    def get_outcome(self):
        pass

    def start(self) -> tuple[str, dict]:
        return "", {}

