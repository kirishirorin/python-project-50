lint:
	poetry run flake8 gendiff

build:
	poetry build

_gendiff:
	poetry run python -m gendiff.scripts.gendiff file1.json file2.json
