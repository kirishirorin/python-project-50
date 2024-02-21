#!/usr/bin/env python3
import argparse
import json


parser = argparse.ArgumentParser(description='Compares two configuration files'
                                 'and shows a difference.')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', type=str, default='FORMAT',
                    help='set format of output')
args = parser.parse_args()


def load_file(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)
        return data


def generate_diff(first_path, second_path):
    first_file_1 = load_file(first_path)
    second_file_2 = load_file(second_path)
    set_file_1 = set(first_file_1.keys()) - set(second_file_2.keys())
    set_file_2 = set(second_file_2.keys()) - set(first_file_1.keys())
    set_file_12 = set(first_file_1.keys()) & set(second_file_2.keys())
    text = []
    if set_file_1:
        for key in set_file_1:
            text.append('- ' + str(key) + ': ' + str(first_file_1[key]))
    if set_file_2:
        for key in set_file_2:
            text.append('+ ' + str(key) + ': ' + str(second_file_2[key]))
    if set_file_12:
        for key in set_file_12:
            if (first_file_1[key] != second_file_2[key]
               and first_file_1 and second_file_2):
                text.append('- ' + str(key) + ': ' + str(first_file_1[key]))
                text.append('+ ' + str(key) + ': ' + str(second_file_2[key]))
            else:
                text.append('  ' + str(key) + ': ' + str(second_file_2[key]))
    text_sorted = sorted(text, key=lambda x: x[2])
    text_sorted.insert(0, '{')
    text_sorted.append('}')
    return print('\n'.join(text_sorted))


if __name__ == '__main__':
    generate_diff(args.first_file, args.second_file)
