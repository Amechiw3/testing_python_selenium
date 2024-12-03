# Define la estructura de carpetas
$folders = @(
    "config",
    "drivers",
    "pages",
    "reports/html",
    "reports/logs",
    "reports/screenshots",
    "tests/auth",
    "tests/search",
    "utils",
    "ci_cd"
)

# Crear carpetas
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder
}

$files = @(
    "config/config.yaml",
    "pages/base_page.py",
    "reports/html/report.html",
    "reports/logs/test.log",
    "reports/screenshots",
    "tests/conftest.py",
    "tests/search",
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