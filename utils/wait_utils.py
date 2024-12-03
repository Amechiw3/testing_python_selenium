from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitUtils:
    """Clase de utilidades para manejar esperas explícitas en Selenium."""
    
    def __init__(self, driver, timeout=10):
        """
        Inicializa la clase con un WebDriver y un tiempo de espera predeterminado.
        
        :param driver: Instancia del WebDriver de Selenium.
        :param timeout: Tiempo máximo de espera en segundos.
        """
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, by, locator):
        """
        Espera a que un elemento sea visible en la página.
        
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :return: WebElement encontrado.
        :raises TimeoutException: Si el elemento no es visible dentro del tiempo límite.
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(f"El elemento con {by}='{locator}' no se hizo visible después de {self.timeout} segundos.")

    def wait_for_element_clickable(self, by, locator):
        """
        Espera a que un elemento sea clickeable.
        
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :return: WebElement encontrado.
        :raises TimeoutException: Si el elemento no es clickeable dentro del tiempo límite.
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(f"El elemento con {by}='{locator}' no fue clickeable después de {self.timeout} segundos.")

    def wait_for_element_present(self, by, locator):
        """
        Espera a que un elemento esté presente en el DOM.
        
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :return: WebElement encontrado.
        :raises TimeoutException: Si el elemento no está presente dentro del tiempo límite.
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(f"El elemento con {by}='{locator}' no estuvo presente en el DOM después de {self.timeout} segundos.")

    def wait_for_text_in_element(self, by, locator, text):
        """
        Espera a que un elemento contenga un texto específico.
        
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :param text: Texto esperado en el elemento.
        :return: True si el texto está presente, de lo contrario TimeoutException.
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.text_to_be_present_in_element((by, locator), text)
            )
        except TimeoutException:
            raise TimeoutException(f"El texto '{text}' no se encontró en el elemento con {by}='{locator}' después de {self.timeout} segundos.")

    def wait_for_element_not_visible(self, by, locator):
        """Espera a que un elemento ya no sea visible."""
        try:
            return WebDriverWait(self.driver, self.timeout).until_not(
                EC.visibility_of_element_located((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(f"El elemento con {by}='{locator}' aún es visible después de {self.timeout} segundos.")

    def wait_for_attribute(self, by, locator, attribute, value):
        """Espera a que un elemento tenga un atributo con un valor específico."""
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.attribute_to_include((by, locator), attribute, value)
            )
        except TimeoutException:
            raise TimeoutException(f"El atributo '{attribute}' del elemento con {by}='{locator}' no contiene el valor '{value}' después de {self.timeout} segundos.")
