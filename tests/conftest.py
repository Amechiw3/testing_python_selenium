import pytest
from datetime import datetime
import os
import yaml
from selenium import webdriver
from _pytest.runner import CallInfo
import base64

@pytest.fixture(scope="session")
def config():
    """Carga la configuración desde el archivo YAML."""
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="function")
def driver(config):
    """Inicializa el navegador según la configuración."""
    browser = config['browser']
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Navegador no soportado: {browser}")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura capturas de pantalla y las adjunta al reporte HTML si hay fallos."""
    outcome = yield
    report = outcome.get_result()

    # Verifica si la prueba falló
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")  # Obtén el driver desde los fixtures
        if driver:
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, screenshot_name)
            driver.save_screenshot(filepath)