lint:
	poetry run flake8 gendiff

build:
	poetry build

_gendiff_json:
	poetry run python -m gendiff.scripts.gendiff file1.json file2.json

_gendiff_yaml:
	poetry run python -m gendiff.scripts.gendiff file1.yaml file2.yaml

testing:
	poetry run pytest

report:
	poetry run pytest --cov
