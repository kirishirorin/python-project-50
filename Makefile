lint:
	poetry run flake8 gendiff

build:
	poetry build

_gendiff_json_plain:
	poetry run python -m gendiff.scripts.gendiff --format plain tests/fixtures/json/file1.json tests/fixtures/json/file2.json

_gendiff_json_stylish:
	poetry run python -m gendiff.scripts.gendiff --format stylish tests/fixtures/json/file1.json tests/fixtures/json/file2.json

_gendiff_json_json:
	poetry run python -m gendiff.scripts.gendiff --format json tests/fixtures/json/file1.json tests/fixtures/json/file2.json

_gendiff_yaml_plain:
	poetry run python -m gendiff.scripts.gendiff --format plain tests/fixtures/yaml/file1.yaml tests/fixtures/yaml/file2.yaml

_gendiff_yaml_stylish:
	poetry run python -m gendiff.scripts.gendiff --format stylish tests/fixtures/yaml/file1.yaml tests/fixtures/yaml/file2.yaml

_gendiff_yaml_json:
	poetry run python -m gendiff.scripts.gendiff --format json tests/fixtures/yaml/file1.yaml tests/fixtures/yaml/file2.yaml

testing:
	poetry run pytest

report:
	poetry run pytest --cov --cov-report=xml ./tests/
