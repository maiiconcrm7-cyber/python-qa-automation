# Python QA Automation | API Testing Portfolio

[![Python QA Automated Tests](https://github.com/maiiconcrm7-cyber/python-qa-automation/actions/workflows/python-app.yml/badge.svg)](https://github.com/maiiconcrm7-cyber/python-qa-automation/actions/workflows/python-app.yml)

A practical Quality Assurance portfolio featuring automated testing with **Python, Pytest, and Postman**.

This project demonstrates API validation, test automation, positive and negative scenarios, and software testing fundamentals.

## Technologies

- Python
- Pytest
- Requests
- Postman
- REST APIs
- Git and GitHub

## Skills Demonstrated

- Automated test development
- API response validation
- HTTP status code testing
- JSON data validation
- Positive and negative test scenarios
- Boundary value analysis
- Test execution and reporting
- Version control with Git

## Python Automated Tests

The Python test suite includes:

- User registration validation
- Required field validation
- Minimum age and boundary testing
- REST API testing
- HTTP response status validation
- JSON field and data type verification
- API response time testing

### Install Dependencies

```bash
python -m pip install pytest requests
```

### Run Automated Tests

```bash
python -m pytest -v
```

### Generate a Test Report

```bash
python -m pytest -v --junitxml=relatorio_testes.xml
```

## Postman API Testing

The Postman collection uses the public JSONPlaceholder API.

**Base URL:** https://jsonplaceholder.typicode.com

### GET — Retrieve User

Endpoint: `GET /users/1`

Automated validations:

- HTTP 200 response
- Correct user name
- Correct email address
- Response time below 1000 ms
- Required JSON properties
- Correct data types

### GET — Nonexistent User

Endpoint: `GET /users/999999`

Automated validations:

- HTTP 404 response
- Empty JSON response

### POST — Create User

Endpoint: `POST /users`

Automated validations:

- HTTP 201 Created
- Correct user name
- Correct email address
- Correct username
- Generated user ID

**Note:** JSONPlaceholder simulates POST operations and does not permanently store the created user.

## Postman Test Results

| Metric | Result |
|---|---|
| API requests | 3 |
| Automated checks | 13 |
| Passed | 13 |
| Failed | 0 |
| Errors | 0 |

These results were recorded during a successful Postman collection run.

## Project Structure

```text
curso_qa_python/
├── cadastro.py
├── teste_cadastro.py
├── test_cadastro_pytest.py
├── test_idades.py
├── test_api.py
├── postman/
│   └── collections/
├── relatorio_testes.xml
└── README.md
```

## Future Improvements

- Expand API test coverage
- Add PUT, PATCH, and DELETE scenarios
- Improve test data management
- Implement GitHub Actions for continuous integration
- Add automated execution reports

## Project Repository

https://github.com/maiiconcrm7-cyber/python-qa-automation

## About This Project

This portfolio was developed as part of hands-on training in software quality assurance and automated testing.

The goal is to demonstrate practical QA skills through reproducible tests, structured validation, and continuous improvement.