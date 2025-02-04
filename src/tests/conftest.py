import base64
import pytest
import pytest_html
import pytest_html.extras
import yaml
import os
from config.driver_manager import DriverManager
from datetime import datetime
from selenium.common.exceptions import WebDriverException

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "environments.yaml")
DEFAULT_SCREENSHOTS_DIR = os.path.join("reports", "screenshots", "failure")

def load_config(env="default"):
    """
    Carga la configuración desde el archivo environments.yaml.
    Devuelve un diccionario con las configuraciones.
    """
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f).get(env, {})

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def driver(config):
    """
    Inicializa y devuelve una instancia del WebDriver configurada.
    Usa DriverManager para manejar el navegador.
    """
    driver_manager = DriverManager(config)
    driver = driver_manager.get_driver()
    env = os.getenv("ENV", "development")
    print(env)
    yield driver
    driver.quit()

def pytest_html_report_title(report):  
    report.title = "Pytest HTML Report" 

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest para capturar el estado de las pruebas y ejecutar acciones en caso de fallo.
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)

@pytest.fixture(scope="function", autouse=True)
def capture_screenshot_on_failure(request, driver, config):
    yield

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshots_dir = config.get('reports', {}).get('failures', DEFAULT_SCREENSHOTS_DIR)
        os.makedirs(screenshots_dir, exist_ok=True)

        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.abspath(os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png"))

        try:
            driver.save_screenshot(screenshot_path)
            print(f"Captura de pantalla guardada: {screenshot_path}")
            print(request)

            if hasattr(request.config, "_html"):
                from pytest_html import extras
                request.config._html.extras.append(extras.png(screenshot_path))
                print(f"Captura de pantalla adjuntada al reporte HTML: {screenshot_path}")
            else:
                print("El reporte HTML no está configurado. No se adjuntó la captura de pantalla.")

        except Exception as e:
            print(f"Error al guardar o adjuntar la captura de pantalla: {e}")
    else:
        print("La prueba no falló, no se capturó ninguna captura de pantalla.")
