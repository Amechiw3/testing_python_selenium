import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.logger import setup_logger

logger = setup_logger()


class DriverManager:
    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"
    DRIVER_PATHS = {
        CHROME: "chromedriver.exe",
        FIREFOX: "geckodriver.exe",
        EDGE: "msedgedriver.exe",
    }

    def __init__(self, config):
        logger.info(f"Inicializando DriverManager con configuración: {config}")
        self.config = config

    def get_driver(self):
        browser = self.config.get("browser", self.CHROME).lower()
        headless = self.config.get("headless", False)

        try:
            if browser == self.CHROME:
                return self._get_chrome_driver(headless)
            elif browser == self.FIREFOX:
                return self._get_firefox_driver(headless)
            elif browser == self.EDGE:
                return self._get_edge_driver(headless)
            else:
                raise ValueError(f"Navegador '{browser}' no está soportado.")
        except Exception as e:
            logger.error(f"Error al inicializar el WebDriver: {e}")
            raise Exception("Error al inicializar el WebDriver")

    def _get_chrome_driver(self, headless):
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": self._get_download_path(),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            },
        )
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # service = ChromeService(executable_path=self._get_driver_path(self.DRIVER_PATHS[self.CHROME]))
        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def _get_firefox_driver(self, headless):
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        # service = FirefoxService(executable_path=self._get_driver_path(self.DRIVER_PATHS[self.FIREFOX]))
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

    def _get_edge_driver(self, headless):
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        service = EdgeService(
            executable_path=self._get_driver_path(self.DRIVER_PATHS[self.EDGE])
        )
        return webdriver.Edge(service=service, options=options)

    @staticmethod
    def _get_driver_path(driver_name):
        """
        Obtiene la ruta absoluta al controlador del navegador.
        :param driver_name: Nombre del controlador (chromedriver, geckodriver, etc.)
        :return: Ruta absoluta del controlador
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, "../drivers", driver_name)

    @staticmethod
    def _get_download_path():
        """
        Obtiene la ruta absoluta al directorio de descargas.
        :return: Ruta absoluta del directorio de descargas
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        download_dir = os.path.join(base_dir, "../drivers/downloads")
        return os.path.realpath(download_dir)
