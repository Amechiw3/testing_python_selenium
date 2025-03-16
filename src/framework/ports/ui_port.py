"""Módulo que define la interfaz que debe ser implementada por cualquier parte de UI.
"""
from abc import ABC, abstractmethod


class UIPort(ABC):
    """Interfaz que define los métodos que deben ser implementados por cualquier parte de UI.
    """
    @abstractmethod
    def configure_logger(self, logger_name, logger_dir):
        """Configura el logger.

        Args:
            logger_name (_type_): Nombre del logger.
            logger_dir (_type_): Directorio donde se guardará el logger.
        """

    @abstractmethod
    def load_data(self, filename):
        """Carga los datos de un archivo YAML.
        """

    @abstractmethod
    def load_lang(self, filename, lang="default"):
        """Carga los datos de un archivo YAML de lenguaje.
        """

    @abstractmethod
    def navigate(self, url):
        """Navega a una URL específica.
        """

    @abstractmethod
    def get_page_title(self):
        """Obtiene el título de la página actual.
        """

    @abstractmethod
    def get_current_url(self):
        """Obtiene la URL actual de la página.
        """

    @abstractmethod
    def find_element(self, locator):
        """Encuentra un elemento único en la página
        """

    @abstractmethod
    def find_elements(self, locator):
        """Encuentra varios elementos en la página.
        """

    @abstractmethod
    def find_element_is_exist(self, locator):
        """Verifica si un elemento existe en la página.
        """

    @abstractmethod
    def click(self, locator):
        """Hace clic en un elemento.

        Args:
            locator (_type_): Localizador del elemento.
        """

    @abstractmethod
    def click_enter(self, locator):
        """Hace clic en un elemento y presiona la tecla Enter.
        """

    @abstractmethod
    def click_few_times(self, locator, times):
        """Hace clic en un elemento varias veces.

        Args:
            locator (_type_): Localizador del elemento.
            times (_type_): Cantidad de veces a hacer clic.
        """
        for _ in range(times):
            self.find_element(locator).click()

    @abstractmethod
    def hover(self, locator):
        """Hace hover sobre un elemento.

        Args:
            locator (_type_): Localizador del elemento.
        """

    @abstractmethod
    def send_keys(self, locator, text):
        """Escribe texto en un campo.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """

    @abstractmethod
    def send_keys_clear(self, locator, text):
        """Escribe texto en un campo y lo limpia antes de escribir.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """

    @abstractmethod
    def send_keys_tab(self, locator, text):
        """Escribe texto en un campo y presiona la tecla Tab.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """

    @abstractmethod
    def send_keys_enter(self, locator, text):
        """Escribe texto en un campo y presiona la tecla Enter.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """

    @abstractmethod
    def send_keys_click(self, locator, text):
        """Escribe texto en un campo y hace clic en el elemento.

        Args:
            locator (_type_): Localizador del campo.
            text (_type_): Texto a escribir.
        """

    @abstractmethod
    def clear(self, locator):
        """Limpia un campo de texto.

        Args:
            locator (_type_): Localizador del campo.
        """

    @abstractmethod
    def get_text(self, locator):
        """Obtiene el texto de un elemento.

        Args:
            locator (_type_): Localizador del elemento.

        Returns:
            _type_: Texto del elemento.
        """

    @abstractmethod
    def get_value(self, locator):
        """Obtiene el valor de un campo de texto.

        Args:
            locator (_type_): Localizador del campo.

        Returns:
            _type_: Valor del campo.
        """

    @abstractmethod
    def swtich_to_frame(self, locator):
        """Cambia al frame especificado.

        Args:
            locator (_type_): Localizador del frame.
        """

    @abstractmethod
    def switch_to_default_content(self):
        """Regresa al contenido principal de la página.
        """

    @abstractmethod
    def switch_to_alert(self):
        """Cambia al alert.

        Returns:
            _type_: Alerta actual.
        """

    @abstractmethod
    def accept_alert(self):
        """Acepta el alert.
        """

    @abstractmethod
    def dismiss_alert(self):
        """Rechaza el alert.
        """

    @abstractmethod
    def get_alert_text(self):
        """Obtiene el texto del alert.

        Returns:
            _type_: Texto del alert.
        """

    @abstractmethod
    def scroll_to_top(self):
        """Hace scroll al inicio de la página.
        """

    @abstractmethod
    def scroll_to_bottom(self):
        """Hace scroll al final de la página.
        """

    @abstractmethod
    def scroll_to_element(self, locator):
        """Hace scroll a un elemento específico.

        Args:
            locator (_type_): Localizador del elemento.
        """

    @abstractmethod
    def scroll_to_element_center(self, locator):
        """Hace scroll al centro de un elemento específico.

        Args:
            locator (_type_): Localizador del elemento.
        """

    @abstractmethod
    def take_screenshot(self, nodo="", name="screenshot"):
        """Toma una captura de pantalla de la página

        Args:
            nodo (str, optional): Directorio donde sera guardada. Defaults to "".
            name (str, optional): Nombre con el cual va ser guardada. Defaults to "screenshot".
        """