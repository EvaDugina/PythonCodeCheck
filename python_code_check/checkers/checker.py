
def convertFiledsOfJsonToCorrectTypes(config_json):
    for key in config_json:
        if config_json[key] == "false" or config_json[key] == "true":
            config_json[key] = config_json[key] == "true"
        elif type(config_json[key]) == str and config_json[key].isdigit():
            config_json[key] = int(config_json[key])
        elif type(config_json[key]) == list and len(config_json[key]) > 0:
            if type(config_json[key][0]) == str:
                continue
            inside_list = list()
            for elem in config_json[key]:
                inside_list.append(convertFiledsOfJsonToCorrectTypes(elem))
            config_json[key] = inside_list
        elif type(config_json[key]) == dict:
            config_json[key] = convertFiledsOfJsonToCorrectTypes(config_json[key])

    return config_json


class Checker:
    _config_json = {}
    _files_to_check = []

    def __init__(self, config_json, files_to_check):
        self._config_json = convertFiledsOfJsonToCorrectTypes(config_json)
        self._files_to_check = files_to_check

    def is_enabled(self) -> bool:
        return self._config_json['enabled']

    def get_flags_from_configuration(self, check_name=None) -> []:
        pass

    def get_check_results(self, current_checks, extended_results) -> dict:
        pass

    def get_outcome(self, check_results: []) -> str:
        pass

    def start(self) -> tuple[dict, str, str]:
        pass
