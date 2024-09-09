# Setup

Virtual environment

```
python -m venv .venv
```

Activate virtual environment

```
source .venv/bin/activate
```

Upgrade pip

```
python install --upgrade pip
```

Install package and deps

```
pip install -e .[dev]
```

## Use

Run tests

```
make test
```

Format code

```
make format
```

Build

```
make build
```
