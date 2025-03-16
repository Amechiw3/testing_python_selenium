"""Módulo para la clase SeleniumAdapter.
"""
import os
from datetime import datetime
import yaml
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from adapters.wait_manager import WaitManager
from framework.ports.ui_port import UIPort


class SeleniumAdapter(UIPort):
    """Clase base para las páginas de la aplicación.

    Args:
        UIPort (_type_): Interfaz de los puertos de la UI.
    """
    def __init__(self, driver, config):
        """Constructor de la clase BasePage.

        Args:
            driver (_type_): Instancia del driver de Selenium.
            config (_type_): Configuración de la aplicación.
        """
        self.driver = driver
        self.config = config
        self.wait_manager = WaitManager(
            driver,
            config.get("timeouts", {}).get("implicit_wait", 20),
            config.get("timeouts", {}).get("explicit_wait", 20)
        )

    def configure_logger(self, logger):
        """Configura el logger.

        Args:
            logger (_type_): Nombre del logger.
        """
        self.logger = logger
        self.wait_manager.configure_logger(logger)

    def load_data(self, filename):
        """Carga los datos de un archivo YAML.

        Args:
            filename (_type_): Nombre del archivo YAML.

        Returns:
            _type_: Diccionario con los datos del archivo YAML.
        """
        self.logger.info(f"Cargando datos del archivo {filename}.yaml")
        data_path = os.path.join(os.path.dirname(__file__), f"../data/{filename}.yaml")
        with open(data_path, "r") as f:
            return yaml.safe_load(f).get("default", {})

    def load_lang(self, filename, lang="default"):
        """Carga los datos de un archivo YAML de lenguaje.

        Args:
            filename (_type_): Nombre del archivo YAML.
            lang (str, optional): _description_. Defaults to "default".

        Returns:
            _type_: Diccionario con los datos del archivo YAML.
        """
        self.logger.info(f"Cargando lenguaje del archivo {filename}.yaml")
        languange_path = os.path.join(os.path.dirname(__file__), f"../lang/{filename}.yaml")
        with open(languange_path, "r") as f:
            return yaml.safe_load(f).get(lang, {})

    def navigate(self, url):
        """Navega a una URL específica.

        Args:
            url (_type_): URL a la que se desea navegar.

        Returns:
            _type_: None
        """
        self.logger.info(f"Navegando a la URL: {url}")
        self.driver.get(url)
        self.driver.execute_script("return document.readyState")

    def get_page_title(self):
        """Obtiene el título de la página actual.

        Returns:
            _type_: Título de la página.
        """
        self.logger.info("Obteniendo el título de la página")
        return self.driver.title

    def get_current_url(self):
        """Obtiene la URL actual de la página.

        Returns:
            _type_: URL actual de la página.
        """
        self.logger.info("Obteniendo la URL actual de la página")
        return self.driver.current_url

    def find_element(self, locator):
        """Encuentra un elemento único en la página

        Args:
            locator (_type_): Localizador del elemento.

        Returns:
            _type_: Elemento encontrado.
        """
        self.logger.info(f"Buscando elemento: {locator}")
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Encuentra varios elementos en la página.

        Args:
            locator (_type_): Localizador de los elementos.

        Returns:
            _type_: Lista de elementos encontrados.
        """
        self.logger.info(f"Buscando elementos: {locator}")
        return self.driver.find_elements(*locator)

    def find_element_is_exist(self, locator):
        """Verifica si un elemento existe en la página.

        Args:
            locator (_type_): Localizador del elemento.

        Returns:
            _type_: True si el elemento existe, False en caso contrario.
        """
        try:
            self.logger.info(f"Verificando si el elemento existe: {locator}")
            self.find_element(locator)
            return True
        except:
            return False

    def click(self, locator):
        """Hace clic en un elemento.

        Args:
            locator (_type_): Localizador del elemento.
        """
        self.logger.info(f"Haciendo clic en el elemento: {locator}")
        self.find_element(locator).click()

    def click_enter(self, locator):
        """Hace clic en un elemento y presiona la tecla Enter.

        Args:
            locator (_type_): Localizador del elemento.
        """
        self.logger.info(f"Haciendo clic en el elemento: {locator}")
        self.find_element(locator).click()
        self.find_element(locator).send_keys(Keys.ENTER)

    def click_few_times(self, locator, times):
        """Hace clic en un elemento varias veces.

        Args:
            locator (_type_): Localizador del elemento.
            times (_type_): Cantidad de veces a hacer clic.
        """
        self.logger.info(f"Haciendo clic en el elemento: {locator} {times} veces")
        for _ in range(times):
            self.find_element(locator).click()

    def hover(self, locator):
        """Hace hover sobre un elemento.

        Args:
            locator (_type_): Localizador del elemento.
        """
        self.logger.info(f"Haciendo hover sobre el elemento: {locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def send_keys(self, locator, text):
        """Escribe texto en un campo.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """
        self.logger.info(f"Escribiendo en el campo: {locator}")
        self.find_element(locator).send_keys(text)

    def send_keys_clear(self, locator, text):
        """Escribe texto en un campo y lo limpia antes de escribir.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """
        self.logger.info(f"Escribiendo en el campo: {locator}")
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    def send_keys_tab(self, locator, text):
        """Escribe texto en un campo y presiona la tecla Tab.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """
        self.logger.info(f"Escribiendo en el campo: {locator}")
        self.find_element(locator).send_keys(text)
        self.find_element(locator).send_keys(Keys.TAB)

    def send_keys_enter(self, locator, text):
        """Escribe texto en un campo y presiona la tecla Enter.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """
        self.logger.info(f"Escribiendo en el campo: {locator}")
        self.find_element(locator).send_keys(text)
        self.find_element(locator).send_keys(Keys.ENTER)

    def send_keys_click(self, locator, text):
        """Escribe texto en un campo y hace clic en el elemento.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """
        self.logger.info(f"Escribiendo en el campo: {locator}")
        self.find_element(locator).click()
        self.find_element(locator).send_keys(text)

    def clear(self, locator):
        """Limpia un campo de texto.

        Args:
            locator (_type_): Localizador del campo.
        """
        self.logger.info(f"Limpiando el campo: {locator}")
        self.find_element(locator).clear()

    def get_text(self, locator):
        """Obtiene el texto de un elemento.

        Args:
            locator (_type_): Localizador del elemento.

        Returns:
            _type_: Texto del elemento.
        """
        self.logger.info(f"Obteniendo el texto del elemento: {locator}")
        return self.find_element(locator).text

    def get_value(self, locator):
        """Obtiene el valor de un campo de texto.

        Args:
            locator (_type_): Localizador del campo.

        Returns:
            _type_: Valor del campo.
        """
        self.logger.info(f"Obteniendo el valor del campo: {locator}")
        return self.find_element(locator).get_attribute("value").strip()

    def swtich_to_frame(self, locator):
        """Cambia al frame especificado.

        Args:
            locator (_type_): Localizador del frame.
        """
        self.logger.info(f"Cambiando al frame: {locator}")
        self.driver.switch_to.frame(self.find_element(locator))

    def switch_to_default_content(self):
        """Regresa al contenido principal de la página.
        """
        self.logger.info("Regresando al contenido principal de la página")
        self.driver.switch_to.default_content()

    def switch_to_alert(self):
        """Cambia al alert.

        Returns:
            _type_: Alerta actual.
        """
        self.logger.info("Cambiando al alert")
        return self.driver.switch_to.alert

    def accept_alert(self):
        """Acepta el alert.
        """
        self.logger.info("Aceptando el alert")
        self.switch_to_alert().accept()

    def dismiss_alert(self):
        """Rechaza el alert.
        """
        self.logger.info("Rechazando el alert")
        self.switch_to_alert().dismiss()

    def get_alert_text(self):
        """Obtiene el texto del alert.

        Returns:
            _type_: Texto del alert.
        """
        self.logger.info("Obteniendo el texto del alert")
        return self.switch_to_alert().text

    def scroll_to_top(self):
        """Hace scroll al inicio de la página.
        """
        self.logger.info("Haciendo scroll al inicio de la página")
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_bottom(self):
        """Hace scroll al final de la página.
        """
        self.logger.info("Haciendo scroll al final de la página")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, locator):
        """Hace scroll a un elemento específico.

        Args:
            locator (_type_): Localizador del elemento.
        """
        self.logger.info(f"Haciendo scroll al elemento: {locator}")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_element_center(self, locator):
        """Hace scroll al centro de un elemento específico.

        Args:
            locator (_type_): Localizador del elemento.
        """
        self.logger.info(f"Haciendo scroll al centro del elemento: {locator}")
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def take_screenshot(self, nodo="", name="screenshot"):
        """Toma una captura de pantalla de la página

        Args:
            nodo (str, optional): Directorio donde sera guardada. Defaults to "".
            name (str, optional): Nombre con el cual va ser guardada. Defaults to "screenshot".
        """
        self.logger.info("Tomando captura de pantalla")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshots_dir = f"reports/screenshots/{nodo}"

        # Crear la carpeta si no existe
        os.makedirs(screenshots_dir, exist_ok=True)

        # Guardar la captura
        filepath = os.path.join(screenshots_dir, screenshot_name)
        self.driver.save_screenshot(filepath)
        self.logger.info(f"Captura guardada: {filepath}")
        print(f"Captura guardada: {filepath}")
