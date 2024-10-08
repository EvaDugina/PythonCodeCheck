from python_code_check.checkers.checker import Checker


class Pyflakes(Checker):
    _name = "pyflakes"

    def __init__(self, config_json, files_to_check):
        super().__init__(config_json, files_to_check)

    def get_args_from_configuration(self):
        return [] + self._files_to_check

    def get_outcome(self):
        pass

    def start(self) -> tuple[str, dict]:
        return "", {}



