#!/usr/bin/env python3
from gendiff.functions.funcs import command_line
from gendiff.functions.funcs import generate_diff


def main():
    args = command_line()
    print(generate_diff(args.first_file, args.second_file, format=args.format))


if __name__ == '__main__':
    main()
