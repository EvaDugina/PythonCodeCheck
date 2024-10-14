
def convertFiledsOfJsonToCorrectTypes(config_json):
    for key in config_json:
        if config_json[key] == "false" or config_json[key] == "true":
            config_json[key] = config_json[key] == "true"
        elif type(config_json[key]) == str and config_json[key].isdigit():
            config_json[key] = int(config_json[key])
        elif type(config_json[key]) == list:
            inside_list = list()
            for elem in config_json[key]:
                inside_list.append( convertFiledsOfJsonToCorrectTypes(elem))
            config_json[key] = inside_list
    return config_json


class Checker:
    _config_json = {}
    _files_to_check = []

    def __init__(self, config_json, files_to_check):
        self._config_json = convertFiledsOfJsonToCorrectTypes(config_json)
        self._files_to_check = files_to_check

    def is_enabled(self) -> bool:
        return self._config_json['enabled']

    def get_flags_from_configuration(self) -> []:
        pass

    def get_check_results(self, current_checks, extended_results) -> dict:
        pass

    def get_outcome(self, check_results) -> str:
        pass

    def start(self) -> tuple[str, dict, str]:
        pass
