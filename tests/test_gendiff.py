from gendiff.scripts.gendiff import generate_diff
import json
import pytest


JSON_PATH = 'tests/fixtures/json'
YAML_PATH = 'tests/fixtures/yaml'
@pytest.mark.parametrize(
    "file1,file2,path,format",
    [
        (
            f"{JSON_PATH}/file1.json",
            f"{JSON_PATH}/file2.json",
            "tests/fixtures/test_answer_stylish.txt",
            "stylish"
        ),
        (
            f"{YAML_PATH}/file1.yaml",
            f"{YAML_PATH}/file2.yaml",
            "tests/fixtures/test_answer_stylish.txt",
            "stylish"
        ),
        (
            f"{JSON_PATH}/file1.json",
            f"{JSON_PATH}/file2.json",
            "tests/fixtures/test_answer_plain.txt",
            "plain"
        ),
        (
            f"{YAML_PATH}/file1.yaml",
            f"{YAML_PATH}/file2.yaml",
            "tests/fixtures/test_answer_plain.txt",
            "plain"
        ),
        (
            f"{JSON_PATH}/file1.json",
            f"{JSON_PATH}/file2.json",
            "tests/fixtures/test_answer_json.txt",
            "json"
        ),
        (
            f"{YAML_PATH}/file1.yaml",
            f"{YAML_PATH}/file2.yaml",
            "tests/fixtures/test_answer_json.txt",
            "json"
        )
    ]
)
def test_generate_diff(file1, file2, path, format):
    with open(path, "r") as test_answer:
        if format != "json":
            answer = test_answer.read()[:-1]
            assert generate_diff(file1, file2, format=format) == answer
        else:
            answer = json.loads(test_answer.read()[:-1])
            assert json.loads(generate_diff(file1, file2, format=format)) == answer
