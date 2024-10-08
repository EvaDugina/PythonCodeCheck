import json

CONFIGURATION_JSON = None
FILES_TO_CHECK = None


def start(configuration):
    global CONFIGURATION_JSON, FILES_TO_CHECK
    CONFIGURATION_JSON = json.load(open(configuration["configuration_file_path"]))
    FILES_TO_CHECK = configuration['check_files']
    check_code()


def check_code():
    print(CONFIGURATION_JSON)
    print(FILES_TO_CHECK)

