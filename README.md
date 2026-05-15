# Selenium UI Automation Framework (Python)

Test automation framework for an e-commerce demo application built with Python, Selenium WebDriver and pytest using Page Object Model (POM).

---

## Tech Stack

- Python 3
- Selenium WebDriver
- pytest
- pytest fixtures
- pytest parameterization
- Faker
- pytest-html

---

## Project Structure

```text
.
├── conftest.py
├── pages
│   ├── components
│   │   ├── filter_component.py
│   │   └── header_component.py
│   ├── account_page.py
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── product_page.py
│   └── registration_page.py
├── tests
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_filtering.py
│   ├── test_login.py
│   ├── test_registration.py
│   └── test_sorting.py
├── test_data
│   └── users.csv
├── utils
│   ├── constants.py
│   ├── csv_reader.py
│   └── data_generator.py
└── reports
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
- Page Components pattern (Header and Filter components)
- pytest fixtures for test setup and dependency injection
- Dynamic test data generation using Faker
- Data-driven testing with pytest parameterization and CSV
- Shared project constants
- HTML reporting with pytest-html

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
pytest
```

Run with detailed output:

```bash
pytest -v
```

Generate HTML report:

```bash
pytest -v --html=reports/report.html
```

Report output:

```text
reports/report.html
```

---

## Notes

This project was created for learning purposes.