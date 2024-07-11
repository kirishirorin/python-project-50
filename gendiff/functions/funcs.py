import argparse
from gendiff.functions.parsing import load_file
from gendiff.formatters.json import json_f
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.functions.diff import show_diff


FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_f
}


def generate_diff(path_file1, path_file2, format='stylish'):
    file1 = load_file(path_file1)
    file2 = load_file(path_file2)
    different = show_diff(file1, file2)
    return FORMATS[format](different)


def read_command_line():
    parser = argparse.ArgumentParser(description='Compares '
                                     'two configuration files'
                                     'and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    return args
