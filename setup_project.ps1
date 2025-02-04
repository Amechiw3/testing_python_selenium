# Define la estructura de carpetas
$folders = @(
    "reports/html",
    "reports/logs",
    "reports/screenshots",
    "src/config",
    "src/data",
    "src/drivers",
    "src/pages",
    "src/tests",
    "src/utils"
)

# Crear carpetas
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder
}

$files = @(
    "reports/html/report.html",
    "reports/logs/test.log",
    "reports/screenshots",
    "src/config/environments.yaml",
    "src/config/driver_manager.py",
    "src/pages/base_page.py",
    "src/pages/login.py",
    "src/pages/navegacion.py",w
    "src/tests/__init__.py",
    "src/tests/conftest.py",
    "src/utils/config.py",
    "src/utils/logger.py",
    "src/utils/wait_utils.py",
    "requirements.txt",
    "pytest.ini",
    "README.md"
)

# Crear files
foreach ($file in $files) {
    New-Item -ItemType File -Force -Path $file
}

Write-Host "Estructura del proyecto creada con éxito."