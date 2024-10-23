import argparse
from python_code_check import codecheck
from python_code_check.error import handle_result


def main():
    parser = argparse.ArgumentParser(prog="python_code_check",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("files", metavar="files", nargs="+",
                        help="paths to test files to check")
    parser.add_argument("-c", "--conf", metavar="config.json",
                        help="path to JSON configuration file", required=True)
    args = parser.parse_args()

    if not args.conf:
        parser.error("path to configuration json file must be provided"
                     "specify it with -c or --conf flags")
    if not args.files:
        parser.error("path to files to check must be provided"
                     "specify it with -t or --test flags")

    config = {
        'configuration_file_path': args.conf,
        'files_to_check': args.files
    }

    # Uncomment code below and comment code above to test without cl args
    # config = {
    #     "configuration_file_path": './examples/EXAMPLE_CONFIG.json',
    #     "files_to_check": ["./examples/lab1/main.py", "./examples/lab1/storage.py"]
    # }

    result = codecheck.start(config)
    print(handle_result(result))


if __name__ == "__main__":
    main()
