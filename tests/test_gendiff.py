#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parsing import load_file


def test_generate_diff():
    with open("tests/fixtures/test_answer.txt", "r") as test_answer:
        test_answer = ''.join(test_answer.readlines())[:-1]
        file1_json = load_file("tests/fixtures/json/file1.json")
        file2_json = load_file("tests/fixtures/json/file2.json")
        file1_yaml = load_file("tests/fixtures/yaml/file1.yaml")
        file2_yaml = load_file("tests/fixtures/yaml/file2.yaml")
        assert generate_diff(file1_json, file2_json) == test_answer
        assert generate_diff(file1_yaml, file2_yaml) == test_answer
