import argparse
import codeCheck


def main():
    # parser = argparse.ArgumentParser(prog="PythonCodeCheck",
    #                                  formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # parser.add_argument("files", metavar="files", nargs="+",
    #                     help="paths to test files to check")
    # parser.add_argument("-c", "--conf", metavar="config.json",
    #                     help="path to JSON configuration file", required=True)
    # args = parser.parse_args()
    #
    # if not args.conf:
    #     parser.error("path to configuration json file must be provided"
    #                  "specify it with -c or --conf flags")
    # if not args.files:
    #     parser.error("path to files to check must be provided"
    #                  "specify it with -t or --test flags")

    # config = {
    #     'configuration_file_path': args.conf,
    #     'check_files': args.files
    # }

    # Uncomment code below and comment code above to test without cl args
    config = {
        "configuration_file_path": './Examples/defaultConfig.json',
        "check_files": ["./Examples/CodeExamples/MediumCode.py"]
    }

    codeCheck.start(config)


if __name__ == "__main__":
    main()
