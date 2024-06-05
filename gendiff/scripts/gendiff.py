#!/usr/bin/env python3
import argparse
from gendiff.scripts.parsing import load_file

def read_bash():
    parser = argparse.ArgumentParser(description='Compares two configuration files'
                                     'and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, default='stylish',
                    help='set format of output')
    args = parser.parse_args()
    return args

def treeing(diction, deeper):
    if isinstance(diction, dict):
        text = []
        deeper_level = deeper * 4 - 2
        for key in diction:
            text.append(f'{" " * deeper_level}  {key}: {treeing(diction[key], deeper + 1) if isinstance(diction[key], dict) else load_file(diction[key], "object")}')
        text_sorted = sorted(text, key=lambda x: x[deeper_level + 2:])
        text_sorted.insert(0, '{')
        text_sorted.append((' ' * (deeper_level - 2)) + '}')
        return '\n'.join(text_sorted)
    else:
        return load_file(diction, "object")


def generate_diff(first_file_1, second_file_2, deeper = 1, format='stylish'):
    text = []
    set_file_1 = set(first_file_1.keys()) - set(second_file_2.keys())
    set_file_2 = set(second_file_2.keys()) - set(first_file_1.keys())
    set_file_12 = set(first_file_1.keys()) & set(second_file_2.keys())
    deeper_level = deeper * 4 - 2
    if set_file_1:
        for key in set_file_1:
            text.append(f'{" " * deeper_level}- {key}: {treeing(first_file_1[key], deeper + 1) if isinstance(first_file_1[key], dict) else load_file(first_file_1[key], "object")}')
    if set_file_2:
        for key in set_file_2:
            text.append(f'{" " * deeper_level}+ {key}: {treeing(second_file_2[key], deeper + 1) if isinstance(second_file_2[key], dict) else load_file(second_file_2[key], "object")}')
    if set_file_12:
        for key in set_file_12:
            if (first_file_1[key] != second_file_2[key]
                and first_file_1 and second_file_2 and deeper > 1):
                text.append(f'{" " * deeper_level}- {key}: {generate_diff(first_file_1[key], second_file_2[key], deeper + 1) if (isinstance(first_file_1[key], dict) and isinstance(second_file_2[key], dict)) else treeing(first_file_1[key], deeper + 1)}')
                text.append(f'{" " * deeper_level}+ {key}: {generate_diff(first_file_1[key], second_file_2[key], deeper + 1) if (isinstance(first_file_1[key], dict) and isinstance(second_file_2[key], dict)) else treeing(second_file_2[key], deeper + 1)}')
            else:
                text.append(f'{" " * deeper_level}  {key}: {generate_diff(first_file_1[key], second_file_2[key], deeper + 1) if (isinstance(first_file_1[key], dict) and isinstance(second_file_2[key], dict)) else treeing(second_file_2[key], deeper + 1)}')
    text_sorted = sorted(text, key=lambda x: x[deeper_level + 2:])
    text_sorted.insert(0, '{')
    text_sorted.append((' ' * (deeper_level - 2)) + '}')
    return '\n'.join(text_sorted)


if __name__ == '__main__':
    args = read_bash()
    first_file_1 = load_file(args.first_file)
    second_file_2 = load_file(args.second_file)
    print(generate_diff(first_file_1, second_file_2, format=args.format))
