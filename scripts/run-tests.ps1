# Go to the project root directory.
Set-Location (Join-Path $PSScriptRoot "..")

$ComposeFile = "docker/docker-compose.yml"
$LogsDirectory = "logs"
$AllureResultsDirectory = "allure-results"

$ExitSuccess = 0
$ExitFailure = 1

function Show-Header {
Write-Host ==========================================
Write-Host Python Selenium Framework
Write-Host Docker Test Runner
Write-Host ==========================================
Write-Host
}

function Show-Step {
    param(
        [string]$Name
    )

    Write-Host "$Name..."
}

function Show-Success {
    Write-Host "[OK] Done"
    Write-Host
}

function Show-Error {
    param(
        [string]$Message
    )

    Write-Host "[ERROR] $Message"
    Write-Host
}

function Run-Step {
    param(
        [string]$Name,
        [string]$LogName,
        [scriptblock]$Command
    )

    Show-Step $Name

    $LogFile = Join-Path $LogsDirectory "$LogName.log"

    & $Command *> $LogFile

    if ($LASTEXITCODE -eq $ExitSuccess) {
        Show-Success
        return $true
    }

    Show-Error "$Name failed."
    Write-Host
    Write-Host "See:"
    Write-Host "$LogFile"
    Write-Host

    return $false
}

function Initialize-Workspace {

    if (Test-Path $LogsDirectory) {
        Remove-Item $LogsDirectory -Recurse -Force
    }

    New-Item -ItemType Directory -Path $LogsDirectory | Out-Null

    if (Test-Path $AllureResultsDirectory) {
        Remove-Item $AllureResultsDirectory -Recurse -Force
    }

    New-Item -ItemType Directory -Path $AllureResultsDirectory | Out-Null
}

function Show-TestSummary {

    $Summary = Get-Content (Join-Path $LogsDirectory "framework.log") |
        Select-String "passed|failed|skipped|error|errors" |
        Select-Object -Last 1
        $Summary = $Summary -replace '^[^|]+\|\s*', ''

    if ($Summary) {
        Write-Host "=========================================="
        Write-Host "Test Summary"
        Write-Host "=========================================="
        Write-Host
        Write-Host $Summary
        Write-Host
    }
}

function Show-AllureMessage {
    Write-Host "Allure results generated."
    Write-Host

    if (Get-Command allure -ErrorAction SilentlyContinue) {

        Write-Host "To view the report, run:"
        Write-Host
        Write-Host "allure serve allure-results"
        Write-Host
    }
    else {

        Write-Host "Allure CLI was not found."
        Write-Host "Install Allure CLI to view the generated report."
        Write-Host
    }
}

function Test-Service {
    param(
        [string]$ServiceName,
        [string]$LogName
    )

    $ContainerId = docker compose -f $ComposeFile ps -q $ServiceName

    if (-not $ContainerId) {
        Show-Error "$ServiceName container was not created."
        Show-LogLocation $LogName
        exit $ExitFailure
    }

    $Status = docker inspect -f "{{.State.Status}}" $ContainerId

    if ($Status -eq "running") {
        return
    }

    Show-Error "$ServiceName failed to start."
    Show-LogLocation $LogName
    exit $ExitFailure
}

function Cleanup {

    Run-Step `
        -Name "Stopping services" `
        -LogName "shutdown" `
        -Command {
            docker compose -f $ComposeFile down
        } | Out-Null
}

function Show-LogLocation {
    param(
        [string]$LogName
    )

    Write-Host "See:"
    Write-Host "$LogsDirectory/$LogName.log"
    Write-Host
}

Initialize-Workspace

try {

    Show-Header

    if (-not (Run-Step `
        -Name "Building framework image" `
        -LogName "build" `
        -Command {
            docker compose -f $ComposeFile build framework
        })) {

        exit $ExitFailure
    }

    if (-not (Run-Step `
        -Name "Starting MariaDB" `
        -LogName "mariadb" `
        -Command {
            docker compose -f $ComposeFile up -d mariadb
    })) {
        exit $ExitFailure
    }

    Test-Service `
        -ServiceName "mariadb" `
        -LogName "mariadb"

    if (-not (Run-Step `
        -Name "Initializing database" `
        -LogName "db-init" `
        -Command {
            docker compose -f $ComposeFile up db-init
    })) {
        exit $ExitFailure
    }

    if (-not (Run-Step `
        -Name "Starting API" `
        -LogName "api" `
        -Command {
            docker compose -f $ComposeFile up -d laravel-api
    })) {
        exit $ExitFailure
    }

    Test-Service `
        -ServiceName "laravel-api" `
        -LogName "api"

    if (-not (Run-Step `
        -Name "Starting Angular" `
        -LogName "angular" `
        -Command {
            docker compose -f $ComposeFile up -d angular-ui
    })) {
        exit $ExitFailure
    }

    Test-Service `
        -ServiceName "angular-ui" `
        -LogName "angular"

    if (-not (Run-Step `
        -Name "Starting Web" `
        -LogName "web" `
        -Command {
            docker compose -f $ComposeFile up -d web
    })) {
        exit $ExitFailure
    }

    Test-Service `
        -ServiceName "web" `
        -LogName "web"

    if (-not (Run-Step `
        -Name "Running tests" `
        -LogName "framework" `
        -Command {
            docker compose -f $ComposeFile up framework
    })) {
        exit $ExitFailure
    }

    Show-TestSummary

    Show-AllureMessage
}
finally {

    Cleanup
}