lint:
	poetry run flake8 gendiff

build:
	poetry build

_gendiff_json:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/json/file1.json tests/fixtures/json/file2.json

_gendiff_yaml:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/yaml/file1.yaml tests/fixtures/yaml/file2.yaml

testing:
	poetry run pytest

report:
	poetry run pytest --cov
