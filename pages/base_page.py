from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        """Navega a una URL específica."""
        self.driver.get(url)

    def find_element(self, locator):
        """Encuentra un elemento único en la página."""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Encuentra múltiples elementos en la página."""
        return self.driver.find_elements(*locator)

    def find_element_is_exist(self, locator):
        """Encuentra un elemento único en la página."""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def click(self, locator):
        """Hace clic en un elemento."""
        self.find_element(locator).click()

    def click_enter(self, locator):
        """Hace clic en un elemento."""
        self.find_element(locator).click()
        self.find_element(locator).send_keys(Keys.ENTER)
    
    def hover(self, locator):
        """Hace hover en un elemento."""
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def send_keys(self, locator, text):
        """Escribe texto en un campo."""
        self.find_element(locator).send_keys(text)
    
    def send_keys_clear(self, locator, text):
        """Escribe texto en un campo."""
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)
    
    def send_keys_tab(self, locator, text):
        """Escribe texto en un campo."""
        self.find_element(locator).send_keys(text)
        self.find_element(locator).send_keys(Keys.TAB)
    
    def send_keys_enter(self, locator, text):
        """Escribe texto en un campo."""
        self.find_element(locator).send_keys(text)
        self.find_element(locator).send_keys(Keys.ENTER)
    
    def send_keys_click(self, locator, text):
        """Escribe texto en un campo."""
        self.find_element(locator).click()
        self.find_element(locator).send_keys(text)
    
    def clear(self, locator):
        """Limpia un campo de texto."""
        self.find_element(locator).clear()

    def get_text(self, locator):
        """Obtiene el texto de un elemento."""
        return self.find_element(locator).text

    def wait_for_element(self, locator, timeout=10):
        """Espera a que un elemento sea visible."""
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def swtich_to_frame(self, locator):
        """Cambia al frame especificado."""
        self.driver.switch_to.frame(self.find_element(locator))

    def switch_to_default_content(self):
        """Regresa al contenido principal de la página."""
        self.driver.switch_to.default_content()

    def take_screenshot(self, nodo = "", name="screenshot"):
        """Captura una captura de pantalla con un nombre único."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshots_dir = f"reports/screenshots/{nodo}"

        # Crear la carpeta si no existe
        os.makedirs(screenshots_dir, exist_ok=True)

        # Guardar la captura
        filepath = os.path.join(screenshots_dir, screenshot_name)
        self.driver.save_screenshot(filepath)
        print(f"Captura guardada: {filepath}")