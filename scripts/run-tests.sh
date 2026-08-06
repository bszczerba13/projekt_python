#!/usr/bin/env bash

set +e

# Go to the project root directory.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

COMPOSE_FILE="docker/docker-compose.yml"
LOGS_DIRECTORY="logs"
ALLURE_RESULTS_DIRECTORY="allure-results"

EXIT_SUCCESS=0
EXIT_FAILURE=1

show_header() {
    echo "=========================================="
    echo "Python Selenium Framework"
    echo "Docker Test Runner"
    echo "=========================================="
    echo
}

show_step() {
    echo "$1..."
}

show_success() {
    echo "[OK] Done"
    echo
}

show_error() {
    echo "[ERROR] $1"
    echo
}

run_step() {
    local name="$1"
    local log_name="$2"
    local command="$3"

    show_step "$name"

    local log_file="$LOGS_DIRECTORY/$log_name.log"

    eval "$command" >"$log_file" 2>&1
    local exit_code=$?

    if [ "$exit_code" -eq "$EXIT_SUCCESS" ]; then
        show_success
        return 0
    fi

    show_error "$name failed."

    echo
    echo "See:"
    echo "$log_file"
    echo

    return 1
}

initialize_workspace() {

    rm -rf "$LOGS_DIRECTORY"
    mkdir -p "$LOGS_DIRECTORY"

    rm -rf "$ALLURE_RESULTS_DIRECTORY"
    mkdir -p "$ALLURE_RESULTS_DIRECTORY"
}

show_test_summary() {

    local summary

    summary=$(grep -E "passed|failed|skipped|error|errors" \
        "$LOGS_DIRECTORY/framework.log" | tail -n 1)

    if [ -n "$summary" ]; then
        echo "=========================================="
        echo "Test Summary"
        echo "=========================================="
        echo
        echo "$summary"
        echo
    fi
}

show_allure_message() {

    echo "Allure results generated."
    echo

    if command -v allure >/dev/null 2>&1; then

        echo "Run:"
        echo
        echo "allure serve allure-results"
        echo

    else

        echo "Allure CLI was not found."
        echo "Install Allure CLI to view the generated report."
        echo

    fi
}

initialize_workspace

show_header

run_step \
    "Building framework image" \
    "build" \
    "docker compose -f $COMPOSE_FILE build framework" \
    || exit $EXIT_FAILURE

run_step \
    "Starting MariaDB" \
    "mariadb" \
    "docker compose -f $COMPOSE_FILE up -d mariadb" \
    || exit $EXIT_FAILURE

run_step \
    "Initializing database" \
    "db-init" \
    "docker compose -f $COMPOSE_FILE up db-init" \
    || exit $EXIT_FAILURE

run_step \
    "Starting API" \
    "api" \
    "docker compose -f $COMPOSE_FILE up -d laravel-api" \
    || exit $EXIT_FAILURE

run_step \
    "Starting Angular" \
    "angular" \
    "docker compose -f $COMPOSE_FILE up -d angular-ui" \
    || exit $EXIT_FAILURE

run_step \
    "Starting Web" \
    "web" \
    "docker compose -f $COMPOSE_FILE up -d web" \
    || exit $EXIT_FAILURE

run_step \
    "Running tests" \
    "framework" \
    "docker compose -f $COMPOSE_FILE up framework" \
    || exit $EXIT_FAILURE

run_step \
    "Stopping services" \
    "shutdown" \
    "docker compose -f $COMPOSE_FILE down" \
    || exit $EXIT_FAILURE

show_test_summary

show_allure_message

exit $EXIT_SUCCESS