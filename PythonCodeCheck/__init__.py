import json


def get_commitizen_config_json():
    commitizen_config_file = open('../.cz.json')
    config_json = json.load(commitizen_config_file)
    commitizen_config_file.close()
    return config_json


commitizen_config_json = get_commitizen_config_json()

__version__ = commitizen_config_json['commitizen']["version"]
