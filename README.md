# Python Selenium Test Automation Framework

Test automation framework for an e-commerce demo application built with Python, Selenium WebDriver and pytest following the Page Object Model (POM) design pattern.

## Technology Stack

- Python
- Selenium WebDriver
- pytest
- Allure Report
- Faker

## Project Structure

```
.
├── pages/              Page Object Model implementation
│   └── components/     Reusable page components
├── test_data/          Test data
├── tests/              Automated test modules
├── utils/              Helper modules
├── config.py           Framework configuration
├── conftest.py         Pytest fixtures and hooks
├── pytest.ini          Pytest configuration
├── requirements.txt    Project dependencies
└── README.md
```

## Framework Features

- Page Object Model (POM)
- Page Components pattern
- pytest fixtures
- Data-driven testing using CSV and pytest parameterization
- Dynamic test data generation using Faker
- Shared project constants
- Explicit waits
- Allure reporting
- Automatic screenshots for failed tests
- Environment information in Allure reports

## Test Coverage

The framework currently automates the following user scenarios:

- User authentication
- Product browsing
- Product filtering
- Product sorting
- Shopping cart management
- Checkout process

> This section will be updated as new test scenarios are implemented.

## Installation

Clone the repository

```bash
git clone https://github.com/bszczerba13/projekt_python.git
```

Go to the project directory

```bash
cd projekt_python
```

(Optional) Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests

```bash
pytest
```

Run tests with verbose output

```bash
pytest -v
```

Generate Allure report

```bash
allure serve allure-results
```

Generate a static Allure report

```bash
allure generate allure-results -o allure-report
```

## Reporting

The framework uses **Allure Report** and provides:

- Interactive test reports
- Automatic screenshots for failed tests
- Environment information
- Detailed execution history
- Test metadata (severity, description, features)

Generated directories:

- `allure-results/` – raw test results
- `allure-report/` – generated static report

## Notes

This project was created for learning purposes.