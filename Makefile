.PHONY: test lint build clean

test:
	tox run -e test

lint: src
	tox run -e lint

build:
	python -m build
	rm -rf src/*egg-info

clean:
	rm -rf dist .tox
