import base64
import pytest
import pytest_html
import yaml
import os
from config.driver_manager import DriverManager
from datetime import datetime

@pytest.fixture(scope="session")
def config():
    """
    Carga la configuración desde el archivo environments.yaml.
    Devuelve un diccionario con las configuraciones.
    """
    config_path = os.path.join(os.path.dirname(__file__), "../config/environments.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f).get("default", {})


@pytest.fixture(scope="session")
def driver(config):
    """
    Inicializa y devuelve una instancia del WebDriver configurada.
    Usa DriverManager para manejar el navegador.
    """
    driver_manager = DriverManager(config)
    driver = driver_manager.get_driver(config)
    driver.implicitly_wait(config.get("implicit_wait", 10))

    yield driver

    # Cerrar el navegador después de todas las pruebas
    driver.quit()

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
    """
    Captura una captura de pantalla si una prueba falla.
    """
    yield
    if request.node.rep_call.failed:
        # Obtener la ruta para guardar las capturas de pantalla
        #screenshots_dir = config.get("screenshots_dir", "reports/screenshots")
        screenshots_dir = f"{config.get('reports', {}).get('screenshots', "reports/screenshots/failure")}/failure"
        os.makedirs(screenshots_dir, exist_ok=True)

        # Generar el nombre del archivo de la captura
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

        # Guardar la captura de pantalla
        driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada: {screenshot_path}")
