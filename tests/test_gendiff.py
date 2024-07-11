#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff
import json
import pytest


@pytest.mark.parametrize("file1,file2,path,format", [("tests/fixtures/json/file1.json", "tests/fixtures/json/file2.json", "tests/fixtures/test_answer_stylish.txt", "stylish"),
                                                     ("tests/fixtures/yaml/file1.yaml", "tests/fixtures/yaml/file2.yaml", "tests/fixtures/test_answer_stylish.txt", "stylish"),
                                                     ("tests/fixtures/json/file1.json", "tests/fixtures/json/file2.json", "tests/fixtures/test_answer_plain.txt", "plain"),
                                                     ("tests/fixtures/yaml/file1.yaml", "tests/fixtures/yaml/file2.yaml", "tests/fixtures/test_answer_plain.txt", "plain"),
                                                     ("tests/fixtures/json/file1.json", "tests/fixtures/json/file2.json", "tests/fixtures/test_answer_json.txt", "json"),
                                                     ("tests/fixtures/yaml/file1.yaml", "tests/fixtures/yaml/file2.yaml", "tests/fixtures/test_answer_json.txt", "json")])
def test_generate_diff(file1, file2, path, format):
    with open(path, "r") as test_answer:
        if format != "json":
            answer = test_answer.read()[:-1]
            assert generate_diff(file1, file2, format=format) == answer
        else:
            answer = json.loads(test_answer.read()[:-1])
            assert json.loads(generate_diff(file1, file2, format=format)) == answer
