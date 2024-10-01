.PHONY: test lint format

test:
	python -m pytest

lint:
	python -m ruff format . --check
	python -m ruff check .
	python -m mypy .

format:
	python -m ruff format
