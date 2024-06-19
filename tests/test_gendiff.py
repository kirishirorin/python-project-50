#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff
import json


def test_generate_diff():
    file1_json = "tests/fixtures/json/file1.json"
    file2_json = "tests/fixtures/json/file2.json"
    file1_yaml = "tests/fixtures/yaml/file1.yaml"
    file2_yaml = "tests/fixtures/yaml/file2.yaml"
    with open("tests/fixtures/test_answer_stylish.txt", "r") as test_answer:
        answer = test_answer.read()[:-1]
        assert generate_diff(file1_json, file2_json, format = 'stylish') == answer
        assert generate_diff(file1_yaml, file2_yaml, format = 'stylish') == answer
    with open("tests/fixtures/test_answer_plain.txt", "r") as test_answer:
        answer = test_answer.read()[:-1]
        assert generate_diff(file1_json, file2_json, format = 'plain') == answer
        assert generate_diff(file1_yaml, file2_yaml, format = 'plain') == answer
    with open("tests/fixtures/test_answer_json.txt", "r") as test_answer:
        answer = json.loads(test_answer.read()[:-1])
        assert json.loads(generate_diff(file1_json, file2_json, format = 'json')) == answer
        assert json.loads(generate_diff(file1_yaml, file2_yaml, format = 'json')) == answer
