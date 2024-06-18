#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parsing import load_file


def test_generate_diff():
    file1_json = load_file("tests/fixtures/json/file1.json")
    file2_json = load_file("tests/fixtures/json/file2.json")
    file1_yaml = load_file("tests/fixtures/yaml/file1.yaml")
    file2_yaml = load_file("tests/fixtures/yaml/file2.yaml")
    with open("tests/fixtures/test_answer_stylish.txt", "r") as test_answer:
        assert generate_diff(file1_json, file2_json, format = 'stylish') == test_answer
        assert generate_diff(file1_yaml, file2_yaml, format = 'stylish') == test_answer
    with open("tests/fixtures/test_answer_plain.txt", "r") as test_answer:
        assert generate_diff(file1_json, file2_json, format = 'plain') == test_answer
        assert generate_diff(file1_yaml, file2_yaml, format = 'plain') == test_answer
    with open("tests/fixtures/test_answer_json.txt", "r") as test_answer:
        assert generate_diff(file1_json, file2_json, format = 'json') == test_answer
        assert generate_diff(file1_yaml, file2_yaml, format = 'json') == test_answer
