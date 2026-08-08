# Python Selenium Test Automation Framework

Test automation framework for an e-commerce demo application built with Python, Selenium WebDriver and pytest following the Page Object Model (POM) design pattern.

The project supports both local execution and Docker-based execution. For Docker environments, helper scripts are provided to automate the complete test workflow.

---

## Technology Stack

- Python
- Selenium WebDriver
- pytest
- Allure Report
- Faker
- Docker
- Docker Compose
- Jenkins
- pytest-xdist

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
- PowerShell and Bash helper scripts
- Allure reporting
- Jenkins CI pipeline with automatic test execution and Allure reporting
- Parallel test execution with 4 workers using pytest-xdist

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

```bash
git clone https://github.com/bszczerba13/projekt_python.git
```

Go to the project directory:

```bash
cd projekt_python
```

---

## Running Tests

The framework supports three execution methods:

### 1. Local execution

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

---

### 2. Docker Compose

#### Prerequisites

- Docker Desktop (Windows) or Docker Engine (Linux)
- Docker Compose

> **Linux (amd64) only**
>
> The project uses a third-party ARM64 Docker image for the `web` service.
> Before running the Docker environment (either manually with Docker Compose or by using the helper script), install QEMU/binfmt support:
>
> ```bash
> docker run --privileged --rm tonistiigi/binfmt --install arm64
> ```

Build the framework image and run the test suite:

```bash
docker compose -f docker/docker-compose.yml up --build framework
```

After the execution completes, stop and remove all containers:

```bash
docker compose -f docker/docker-compose.yml down
```

---

### 3. Helper scripts (Recommended)

The helper scripts automatically perform the following tasks:

- Build the framework image
- Start all required Docker services
- Execute the complete test suite
- Generate Allure results
- Stop and remove all containers
- Save logs for every execution step

#### Windows

```powershell
.\scripts\run-tests.ps1
```

#### Linux

```bash
./scripts/run-tests.sh
```

---

## Reporting

The framework uses **Allure Report** and provides:

- Interactive test reports
- Automatic screenshots for failed tests
- Environment information
- Detailed execution history
- Test metadata (severity, description, features)

View the report:

```bash
allure serve allure-results
```

> The helper scripts automatically clean the `allure-results` directory before each execution.

---

## Continuous Integration

The project includes a Jenkins CI pipeline that automatically runs the test suite after changes are pushed to GitHub.

Test results are published as Allure reports in Jenkins.

---

## Logs

When a Docker execution step fails, the helper scripts save detailed logs in the `logs` directory and display the location of the relevant log file to simplify troubleshooting.

---

## Notes

This project was created for learning purposes.