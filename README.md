### Hexlet tests and linter status:
[![Actions Status](https://github.com/kirishirorin/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kirishirorin/python-project-50/actions)
[Difference 2 files](https://asciinema.org/a/5onMpWTHE45tYIRZFK6wiFSuy)
[![Maintainability](https://api.codeclimate.com/v1/badges/5780225e7f25516a469d/maintainability)](https://codeclimate.com/github/kirishirorin/python-project-50/maintainability)
[How json and yaml works](https://asciinema.org/a/eQKkjFs3Jw01inOtFuOD7k7oO)

Dependencies:
1 python = "^3.10"
2 pyyaml = "^6.0.1"
3 pytest-cov = "^5.0.0"
4 flake8 = "^7.0.0"
5 pytest = "^8.0.1"

How to start using:
1) pip install poetry
2) poetry install
3) poetry run python -m gendiff.scripts.gendiff --format [stylish/plain/json] path1 path2
stylish - Recursive comparison
plain - Flat format
json - Output to JSON
