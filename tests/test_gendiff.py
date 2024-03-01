#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    with open("tests/fixtures/test_answer.txt", "r") as test_answer:
        assert generate_diff("file1.json", "file2.json") == '\n'.join(test_answer.readlines())
