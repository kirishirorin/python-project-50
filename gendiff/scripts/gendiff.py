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
    parser = argparse.ArgumentParser(description='Compares two configuration files'
                                     'and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    return args


def generate_diff(file1, file2, format='stylish'):
    different = diff(file1, file2)
    return OPTION[format](different)


if __name__ == '__main__':
    args = read_bash()
    first_file_1 = load_file(args.first_file)
    second_file_2 = load_file(args.second_file)
    print(generate_diff(first_file_1, second_file_2, format=args.format))
