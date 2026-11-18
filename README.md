
# Python QA Automation | Testing Portfolio

[![Python QA Automated Tests](https://github.com/maiiconcrm7-cyber/python-qa-automation/actions/workflows/python-app.yml/badge.svg)](https://github.com/maiiconcrm7-cyber/python-qa-automation/actions/workflows/python-app.yml)

## About This Project

A hands-on Quality Assurance portfolio focused on
automated software testing using Python and pytest.

This project demonstrates API testing, functional
validation, bug reporting, regression testing,
data-driven testing, and continuous integration.

The projects were developed as educational
simulations to demonstrate practical QA skills.

## Technologies

- Python
- pytest
- Requests
- Postman
- REST APIs
- Git and GitHub
- GitHub Actions
- CSV
- HTML and XML test reports

## Test Coverage

The automated test suite includes:

- User registration validation
- Required field testing
- Minimum age validation
- Boundary value analysis
- Positive and negative test scenarios
- HTTP status code validation
- JSON response validation
- API response time testing
- API data type verification
- GET, POST, PUT and DELETE requests
- pytest fixtures
- CSV-driven testing
- Shopping cart calculation testing
- Regression testing

## Automated Test Results

Latest verified local execution:

| Metric | Result |
|---|---|
| Automated tests | 34 |
| Passed | 34 |
| Failed | 0 |
| Framework | pytest |

The GitHub Actions workflow also completed
successfully after the latest project update.

## Project 1 - REST API Testing

Automated API tests using the public
JSONPlaceholder API.

Base URL:
https://jsonplaceholder.typicode.com

Test scenarios include:

- Retrieve existing users
- Validate user names and email addresses
- Verify nonexistent users return HTTP 404
- Validate HTTP response times
- Check JSON field types
- Simulate user creation with POST
- Simulate user updates with PUT
- Simulate user deletion with DELETE

Note: JSONPlaceholder simulates write operations
without permanently storing changes.

## Project 2 - User Registration Testing

Functional testing of a Python registration
system.

Scenarios include:

- Valid user registration
- Underage user rejection
- Minimum age boundary validation
- Empty name validation
- Positive and negative test cases

## Project 3 - CSV Data-Driven Testing

Automated tests using external CSV data.

The test suite reads user information from
dados_teste.csv and validates registration
results using pytest parametrization.

This approach supports testing multiple
scenarios without duplicating test functions.

## Project 4 - Shopping Cart Testing

An educational e-commerce QA simulation.

Business rules:

- Product price: $50
- Total = price multiplied by quantity
- Zero and negative quantities are rejected

A deliberate calculation bug was introduced
when the quantity was three.

Expected result: $150
Actual result before fix: $100

Initial execution:
4 passed, 1 failed.

After correcting the calculation:
5 passed, 0 failed.

The fix was verified through regression testing.

Bug documentation:
[Shopping Cart Bug Report](BUG_REPORT.md)

## Postman API Testing

The Postman collection covers API requests
using JSONPlaceholder.

Previously recorded collection results:

| Metric | Result |
|---|---|
| API requests | 3 |
| Automated checks | 13 |
| Passed | 13 |
| Failed | 0 |

These results refer to a separate Postman
collection execution.

## Continuous Integration

GitHub Actions automatically runs the
Python test suite when changes are pushed
to the main branch or submitted through
a pull request targeting main.

The workflow:

1. Checks out the repository
2. Configures Python 3.11
3. Installs required dependencies
4. Executes automated pytest tests
5. Generates an HTML report
6. Uploads the report as an artifact

Workflow:
[Python QA Automated Tests](https://github.com/maiiconcrm7-cyber/python-qa-automation/actions)

## Installation

Install the required dependencies:

```bash
python -m pip install pytest requests pytest-html
```

## Run Automated Tests

```bash
python -m pytest -v
```

## Generate HTML Report

```bash
python -m pytest -v --html=relatorio_qa.html --self-contained-html
```

## Generate XML Report

```bash
python -m pytest -v --junitxml=relatorio_testes.xml
```

## Main Project Files

- cadastro.py
- carrinho.py
- test_api.py
- test_cadastro_pytest.py
- test_dados_csv.py
- test_idades.py
- test_carrinho.py
- dados_teste.csv
- BUG_REPORT.md
- README.md
- .github/workflows/python-app.yml

## Skills Demonstrated

- Test case design
- Automated testing
- API testing
- Functional testing
- Regression testing
- Bug identification and documentation
- Boundary value analysis
- Test data management
- Continuous integration
- Technical documentation in English

## Future Improvements

- Expand negative API test coverage
- Add authentication testing scenarios
- Improve fixture reuse
- Introduce API mocking
- Explore Selenium or Playwright
- Expand automated regression coverage

## Repository

https://github.com/maiiconcrm7-cyber/python-qa-automation

## Portfolio Note

This is an educational QA Automation portfolio
demonstrating practical testing workflows.

The shopping cart defect was intentionally
introduced and corrected as part of training.
