
# Python QA Automation - Registration Testing

A beginner QA automation project using Python and Pytest.

## Project Overview

This project tests a simple user registration function.

## Test Scenarios

- Successful registration
- Empty name validation
- Minimum age validation
- Boundary value testing (17, 18, 19)
- Parameterized tests with Pytest

## Technologies

- Python
- Pytest
- Git

## Run Tests

Install Pytest:

python -m pip install pytest

Run all tests:

python -m pytest -v

Generate JUnit XML report:

python -m pytest -v --junitxml=relatorio_testes.xml

## Test Results

11 automated test cases passed during local execution.

## Author

Maicon do Nascimento Silva
