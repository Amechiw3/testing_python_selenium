import pytest
import yaml
import os
from adapters.selenium_adapter import SeleniumAdapter
from config.driver_manager import DriverManager
from datetime import datetime

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config/environments.yaml")
DEFAULT_SCREENSHOTS_DIR = "reports/screenshots/failure"


def load_config(env):
    """Carga la configuración de la prueba desde un archivo YAML.

    Args:
        env (str): El ambiente de la prueba (qa, dev, prod).

    Returns:
        dict: Diccionario con la configuración de la prueba.
    """
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f).get(env, {})


@pytest.fixture(scope="session")
def config(pytestconfig):
    """Fixture de Pytest para cargar la configuración de la prueba.

    Args:
        pytestconfig: Configuración de pytest.

    Returns:
        dict: Diccionario con la configuración de la prueba.
    """
    env = pytestconfig.getoption("env")
    return load_config(env)


@pytest.fixture(scope="session")
def driver(config):
    """Fixture de Pytest para inicializar el WebDriver.

    Args:
        config (_type_): Configuración de la prueba.

    Yields:
        _type_: WebDriver.
    """
    driver_manager = DriverManager(config)
    web_driver = driver_manager.get_driver()
    web_driver.implicitly_wait(config.get("timeouts", {}).get("implicit_wait", 20))

    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="function")
def ui_adapter(driver, config, request):
    """Fixture de Pytest para inicializar el adaptador de la interfaz de usuario.

    Args:
        driver (_type_): WebDriver.
        config (_type_): Configuración de la prueba.

    Returns:
        _type_: Adaptador de la interfaz de usuario.
    """
    # logger_name = request.node.name
    return SeleniumAdapter(driver, config)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Hook de pytest para configurar las opciones de reporte HTML y JUnit XML.

    Args:
        config (_type_): Configuración de pytest.
    """
    datenow = datetime.now().date()
    timestamp = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    html_report = f"reports/html/{datenow}/report_{timestamp}.html"
    junit_report = f"reports/xml/junit/{datenow}/report_{timestamp}.xml"
    # nunit_report = f"reports/xml/nunit/{datenow}/report_{timestamp}.xml"

    # Añadir las opciones de reporte HTML y JUnit XML dinámicamente
    config.option.htmlpath = html_report
    config.option.self_contained_html = True

    config.option.xmlpath = junit_report
    config.option.junit_family = "junit4"
    config.option.junit_logging = "all"
    config.option.junit_log_passing_tests = True
    config.option.junit_log_skipped_tests = True
    config.option.junit_log_deselected_tests = True
    config.option.junit_log_failed_tests = True
    config.option.junit_log_error_tests = True
    config.option.junit_log_crashed_tests = True
    config.option.junit_log_inactive_tests = True


def pytest_html_report_title(report):
    """Hook de pytest-html para establecer el título del reporte HTML.

    Args:
        report (_type_): Reporte de pytest.
    """
    report.title = "Pytest HTML Report"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook de pytest para capturar el estado de las pruebas y ejecutar acciones en caso de fallo.

    Args:
        item (_type_): Item de la prueba.
        call (_type_): Llamada a la prueba.
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture(scope="function", autouse=True)
def capture_screenshot_on_failure(request, driver, config):
    """Fixture de Pytest para capturar una captura de pantalla en caso de fallo.

    Args:
        request (_type_): Request de la prueba.
        driver (_type_): WebDriver.
        config (_type_): Configuración de la prueba.
    """
    yield
    if request.node.rep_call.failed:
        # Obtener la ruta para guardar las capturas de pantalla
        datenow = datetime.now().date()

        screenshots_dir = f"{config.get('reports', {}).get('failures', DEFAULT_SCREENSHOTS_DIR)}/{datenow}"
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


def pytest_addoption(parser):
    """Hook de pytest para añadir opciones de línea de comandos.

    Args:
        parser: Parser de pytest.
    """
    parser.addoption("--env", action="store", default="default", help="Ambientes de las pruebas (qa, dev, prod).")