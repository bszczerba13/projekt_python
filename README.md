# Python Selenium Test Automation Framework

Test automation framework for an e-commerce demo application built with Python, Selenium WebDriver and pytest following the Page Object Model (POM) design pattern.

The project supports both local execution and Docker-based execution. For Docker environments, helper scripts are provided to automate the complete test workflow.

---

## Technology Stack

- Python
- Selenium WebDriver
- pytest
- pytest-xdist
- Allure Report
- Faker
- Docker
- Docker Compose
- Jenkins

---

## Framework Features

- Page Object Model (POM)
- Page Components pattern
- pytest fixtures
- Data-driven testing using CSV and pytest parameterization
- Dynamic test data generation using Faker
- Shared project constants
- Explicit waits
- Automatic screenshots for failed tests
- Environment information in Allure reports
- Docker-based test execution
- Local and Docker cross-browser execution (Chrome, Firefox and Edge)
- Parallel test execution with 4 workers using pytest-xdist
- PowerShell and Bash helper scripts
- Allure reporting
- Jenkins CI pipeline with automatic test execution and Allure reporting

---

## Project Structure

```text
.
├── docker/             Docker Compose configuration
├── jenkins/            Jenkins CI configuration
├── pages/              Page Object Model implementation
│   └── components/     Reusable page components
├── scripts/            Docker helper scripts
├── test_data/          Test data
├── tests/              Automated test modules
├── utils/              Helper modules
├── config.py           Framework configuration
├── conftest.py         Pytest fixtures and hooks
├── pytest.ini          Pytest configuration
├── requirements.txt    Project dependencies
├── Jenkinsfile         Jenkins pipeline definition
└── README.md
```

---

## Test Coverage

The framework currently automates the following user scenarios:

- User authentication
- Product browsing
- Product filtering
- Product sorting
- Shopping cart management
- Checkout process

---

## Installation

Clone the repository:

    git clone https://github.com/bszczerba13/projekt_python.git

Go to the project directory:

    cd projekt_python

---

## Running Tests

### Parallel test execution

Tests are executed in parallel using 4 workers with pytest-xdist to reduce execution time.

The framework supports three execution methods:

1. Local execution
2. Docker Compose
3. Helper scripts

Chrome is used as the default browser. Firefox and Edge can be selected when needed.

---

### 1. Local execution

Create and activate a virtual environment:

#### Windows

    python -m venv .venv
    
    .venv\Scripts\Activate.ps1

#### Linux

    python3 -m venv .venv
    
    source .venv/bin/activate


Install the project dependencies:

    pip install -r requirements.txt

#### Browser selection

Chrome is used by default. To run tests with another browser, set the BROWSER environment variable.

| Browser | PowerShell | Bash |
|---|---|---|
| Chrome | pytest | pytest |
| Firefox | $env:BROWSER="firefox"; pytest | BROWSER=firefox pytest |
| Edge | $env:BROWSER="edge"; pytest | BROWSER=edge pytest |

---

### 2. Docker Compose

#### Prerequisites

- Docker Desktop (Windows) or Docker Engine (Linux)
- Docker Compose

> Linux (amd64) only
>
> The project uses a third-party ARM64 Docker image for the web service.
> Before running the Docker environment (either manually with Docker Compose or by using the helper script), install QEMU/binfmt support:
>
>     docker run --privileged --rm tonistiigi/binfmt --install arm64

#### Run tests

Chrome is used by default. To run tests using another browser, set the BROWSER environment variable before starting the framework.

| Browser | PowerShell | Bash |
|---|---|---|
| Chrome | docker compose -f docker/docker-compose.yml up --build framework | docker compose -f docker/docker-compose.yml up --build framework |
| Firefox | $env:BROWSER="firefox"; docker compose -f docker/docker-compose.yml up --build framework | BROWSER=firefox docker compose -f docker/docker-compose.yml up --build framework |
| Edge | $env:BROWSER="edge"; docker compose -f docker/docker-compose.yml up --build framework | BROWSER=edge docker compose -f docker/docker-compose.yml up --build framework |

After the execution completes, stop and remove all containers:

    docker compose -f docker/docker-compose.yml down

---

### 3. Helper scripts (Recommended)

The helper scripts provide the easiest way to run the complete Docker test workflow.

They automatically:

- Build the framework image
- Start all required Docker services
- Execute the complete test suite
- Generate Allure results
- Stop and remove all containers
- Save logs for every execution step


Chrome is used by default. Firefox and Edge can be selected using the commands below.

| Browser | Windows | Linux |
|---|---|---|
| Chrome | .\scripts\run-tests.ps1 | ./scripts/run-tests.sh |
| Firefox | .\scripts\run-tests.ps1 -Browser firefox | ./scripts/run-tests.sh firefox |
| Edge | .\scripts\run-tests.ps1 -Browser edge | ./scripts/run-tests.sh edge |

---

## Reporting

The framework uses Allure Report and provides:

- Interactive test reports
- Automatic screenshots for failed tests
- Environment information
- Detailed execution history
- Test metadata (severity, description, features)

View the report:

    allure serve allure-results

> Allure CLI is optional and is required only to view the generated reports.

> The helper scripts automatically clean the allure-results directory before each execution.

---

## Continuous Integration

The project includes a Jenkins CI pipeline that automatically runs the test suite after changes are pushed to GitHub.

Test results are published as Allure reports in Jenkins.

---

## Logs

When a Docker execution step fails, the helper scripts save detailed logs in the logs directory and display the location of the relevant log file to simplify troubleshooting.

---

## Notes

This project was created for learning purposes.
