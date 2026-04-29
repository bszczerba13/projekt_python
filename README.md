# Selenium UI Automation Framework (Python)

Test automation framework for an e-commerce demo application built with Python, Selenium WebDriver and unittest using Page Object Model (POM).

---

## Tech Stack

- Python 3
- Selenium WebDriver
- unittest
- DDT
- Faker
- HTMLTestRunner

---

## Project Structure

```text
.
├── pages/          # Page Object classes
├── tests/          # Automated test cases
├── utils/          # Test data generators and helpers
├── test_data/      # CSV test data
├── reports/        # HTML test reports
└── run_tests.py    # Test runner for HTML reports
```

---

## Test Coverage

Implemented automated UI tests for:

- Login (positive and negative scenarios)
- User registration (positive and negative scenarios)
- Product sorting
- Product filtering
- Shopping cart operations
- Guest checkout flow

---

## Framework Features

- Page Object Model (POM)
- Dynamic test data generation using Faker
- Data-driven testing with DDT and CSV
- HTML test reporting

---

## Installation

Clone repository:

```bash
git clone https://github.com/bszczerba13/projekt_python.git
cd projekt_python
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:

```bash
python -m unittest discover tests -v
```

Generate HTML report:

```bash
python run_tests.py
```

Report output:

```text
reports/tests_report.html
```

---

## Notes

This project was created for learning purposes.