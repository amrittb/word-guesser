import argparse
import json
import os
from pathlib import Path


def dir_path(string):
    if string is None:
        raise NotADirectoryError(string)

    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-i", "--input-dir", required=True, help="Files of this directory will be read recursively.", type=dir_path)

    arguments = arg_parser.parse_args()

    input_dir = arguments.input_dir

    text = []
    for path in Path(input_dir).rglob('*'):
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    print(line)
                    text.append(json.loads(line)["text"])

            print(text)
            break


if __name__ == "__main__":
    main()
