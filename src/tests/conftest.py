import pytest
import yaml
import os
from config.driver_manager import DriverManager
from datetime import datetime

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config/environments.yaml")
DEFAULT_SCREENSHOTS_DIR = "reports/screenshots/failure"


def load_config():
    """
    Carga la configuración desde el archivo environments.yaml.
    Devuelve un diccionario con las configuraciones.
    """
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f).get("default", {})


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
    driver.implicitly_wait(config.get("timeouts", {}).get("implicit_wait", 20))

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Hook de pytest para configurar las opciones de reporte HTML y JUnit XML.

    Args:
        config (_type_): Configuración de pytest.
    """
    datenow = datetime.now().date()
    timestamp = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    html_report = f"reports/html/{datenow}/report_{timestamp}.html"
    junit_report = f"reports/xml/{datenow}/report_{timestamp}.xml"

    # Añadir las opciones de reporte HTML y JUnit XML dinámicamente
    config.option.htmlpath = html_report
    config.option.self_contained_html = True
    config.option.xmlpath = junit_report


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
    """
    Captura una captura de pantalla si una prueba falla.
    """
    yield
    if request.node.rep_call.failed:
        # Obtener la ruta para guardar las capturas de pantalla
        screenshots_dir = config.get("reports", {}).get(
            "failures", DEFAULT_SCREENSHOTS_DIR
        )
        os.makedirs(screenshots_dir, exist_ok=True)

        # Generar el nombre del archivo de la captura
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

        # Guardar la captura de pantalla
        try:
            driver.save_screenshot(screenshot_path)
            print(f"Captura de pantalla guardada: {screenshot_path}")
        except Exception as e:
            print(f"Error al guardar la captura de pantalla: {e}")
