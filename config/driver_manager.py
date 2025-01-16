from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import os
from utils.logger import setup_logger

logger = setup_logger()

class DriverManager:
    def __init__(self, config):
        #logger.info(f"Inicializando DriverManager con configuración: {config}")
        self.config = config

    def get_driver(self, config):
        browser = self.config.get("browser", "chrome").lower()
        headless = self.config.get("headless", False)
        selenium_grid_url = self.config.get("selenium_grid_url", None)
        logger.info(f"Inicializando DriverManager con configuración: {config}")

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            # options.add_argument("--window-size=1920,1080")
            options.add_argument("--start-maximized")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            
            # Considerar Responsive

            service = ChromeService(executable_path=self._get_driver_path("chromedriver.exe"))
            return webdriver.Chrome(service=service, options=options)
        
        elif browser == "edge":
            options = EdgeOptions()
            options.add_argument("--start-maximized")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            service = EdgeService(executable_path=self._get_driver_path("msedgedriver.exe"))
            return webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Navegador '{browser}' no está soportado.")

    @staticmethod
    def _get_driver_path(driver_name):
        """
        Obtiene la ruta absoluta al controlador del navegador.
        :param driver_name: Nombre del controlador (chromedriver, geckodriver, etc.)
        :return: Ruta absoluta del controlador
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        driver_path = os.path.join(base_dir, "../drivers", driver_name)

        # Verifica si el archivo existe
        if not os.path.isfile(driver_path):
            raise ValueError(f"El archivo no es un archivo válido: {driver_path}")
        
        return driver_path
