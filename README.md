# ci-fix-test-repo

A simple Python project demonstrating unit tests and CI/CD with GitHub Actions using `uv` as the package manager.

## Features

- Python 3.12
- Package management with `uv`
- Unit tests with `pytest`
- Automated CI/CD with GitHub Actions
- Sample calculator module

## Installation

This project uses [uv](https://docs.astral.sh/uv/) as the package manager. If you don't have uv installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install dependencies:

```bash
uv sync
```

## Running Tests

To run the test suite:

```bash
uv run pytest
```

For verbose output:

```bash
uv run pytest -v
```

## Project Structure

```
.
├── src/
│   └── ci_fix_test_repo/
│       ├── __init__.py
│       └── calculator.py       # Calculator module with basic operations
├── tests/
│   ├── __init__.py
│   └── test_calculator.py      # Unit tests for calculator
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI workflow
├── pyproject.toml              # Project configuration
└── README.md

```

## CI/CD

This repository includes a GitHub Actions workflow that automatically runs tests on:
- Every push to `main` branch
- Every pull request to `main` branch

[![CI](https://github.com/YOUR_USERNAME/ci-fix-test-repo/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/ci-fix-test-repo/actions/workflows/ci.yml)
