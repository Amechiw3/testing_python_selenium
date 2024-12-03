from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        """Navega a una URL específica."""
        self.driver.get(url)

    def find_element(self, locator):
        """Encuentra un elemento único en la página."""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Encuentra múltiples elementos en la página."""
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """Hace clic en un elemento."""
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        """Escribe texto en un campo."""
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        """Obtiene el texto de un elemento."""
        return self.find_element(locator).text

    def wait_for_element(self, locator, timeout=10):
        """Espera a que un elemento sea visible."""
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def take_screenshot(self, name="screenshot"):
        """Captura una captura de pantalla con un nombre único."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshots_dir = "reports/screenshots"

        # Crear la carpeta si no existe
        os.makedirs(screenshots_dir, exist_ok=True)

        # Guardar la captura
        filepath = os.path.join(screenshots_dir, screenshot_name)
        self.driver.save_screenshot(filepath)
        print(f"Captura guardada: {filepath}")