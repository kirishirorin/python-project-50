#!/usr/bin/env python3
import argparse
from gendiff.scripts.parsing import load_file
from gendiff.scripts.json import json_f
from gendiff.scripts.stylish import stylish
from gendiff.scripts.plain import plain
from gendiff.scripts.diff import diff


OPTION = {
    'stylish': stylish,
    'plain': plain,
    'json': json_f
}


def read_bash():
    parser = argparse.ArgumentParser(description='Compares '
                                     'two configuration files'
                                     'and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    return args


def generate_diff(path_file1, path_file2, format='stylish'):
    file1 = load_file(path_file1)
    file2 = load_file(path_file2)
    different = diff(file1, file2)
    return OPTION[format](different)


def main():
    args = read_bash()
    print(generate_diff(args.first_file, args.second_file, format=args.format))


if __name__ == '__main__':
    main()
