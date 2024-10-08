class Checker:
    _config_json = {}
    _files_to_check = []

    def __init__(self, config_json, files_to_check):
        self._config_json = config_json
        self._files_to_check = files_to_check

    def is_enabled(self):
        return self._config_json['enabled']

    def get_args_from_configuration(self):
        pass

    def get_outcome(self):
        pass

    def start(self) -> tuple[str, dict, str]:
        pass
