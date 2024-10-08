import json


def get_commitizen_config_json():
    with open('../.cz.json', encoding="utf-8") as commitizen_config_file:
        return json.load(commitizen_config_file)


commitizen_config_json = get_commitizen_config_json()

__version__ = commitizen_config_json['commitizen']["version"]
