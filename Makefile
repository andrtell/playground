.PHONY: test lint build clean

test:
	python -m pytest

lint:
	python -m ruff format . --check
	python -m ruff check .
	python -m mypy .

init:
	python -m venv .venv

pip:
	python -m pip install -e .[dev]

build:
	python -m build
	rm -rf src/*egg-info

format:
	python -m ruff format

clean:
	rm -rf dist .tox
