# Define la estructura de carpetas
$folders = @(
    "config",
    "data",
    "drivers",
    "pages",
    "reports/html",
    "reports/logs",
    "reports/screenshots",
    "tests",
    "utils"
)

# Crear carpetas
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder
}

$files = @(
    "config/environments.yaml",
    "config/driver_manager.py",
    "pages/base_page.py",
    "pages/login.py",
    "pages/navegacion.py",
    "reports/html/report.html",
    "reports/logs/test.log",
    "reports/screenshots",
    "tests/__init__.py",
    "tests/conftest.py",
    "utils/config.py",
    "utils/logger.py",
    "utils/wait_utils.py",
    "requirements.txt",
    "pytest.ini",
    "README.md"
)

# Crear files
foreach ($file in $files) {
    New-Item -ItemType File -Force -Path $file
}

Write-Host "Estructura del proyecto creada con éxito."