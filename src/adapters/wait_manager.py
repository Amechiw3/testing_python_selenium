
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WaitManager:
    """Clase de utilidades para manejar esperas explícitas en Selenium."""

    def __init__(self, driver, implicitly_wait=10, explicit_wait=20):
        """
        Inicializa la clase con un WebDriver y un tiempo de espera predeterminado.
        :param driver: Instancia del WebDriver de Selenium.
        :param implicitly_wait: Tiempo máximo de espera en segundos.
        """
        self.driver = driver
        self.implicitly_wait = implicitly_wait
        self.explicit_wait = explicit_wait

    def configure_logger(self, logger):
        """Configura un logger para la clase.

        Args:
            logger (_type_): Logger configurado.
        """
        self.logger = logger

    def wait_for_element_visible(self, by, locator):
        """
        Espera a que un elemento sea visible en la página.
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :return: WebElement encontrado.
        :raises TimeoutException: Si el elemento no es visible dentro del tiempo límite.
        """
        try:
            self.logger.info(f"Esperando a que el elemento con {by}='{locator}' sea visible.")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                EC.visibility_of_element_located((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(
                f"El elemento con {by}='{locator}' no se hizo visible después de {self.explicit_wait} segundos."
            )

    def wait_for_element_clickable(self, by, locator):
        """
        Espera a que un elemento sea clickeable.
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :return: WebElement encontrado.
        :raises TimeoutException: Si el elemento no es clickeable dentro del tiempo límite.
        """
        try:
            self.logger.info(f"Esperando a que el elemento con {by}='{locator}' sea clickeable.")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                EC.element_to_be_clickable((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(
                f"El elemento con {by}='{locator}' no fue clickeable después de {self.explicit_wait} segundos."
            )

    def wait_for_element_typing(self, by, locator):
        """
        Espera a que un elemento esté listo para escribir texto.
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :return: WebElement encontrado.
        :raises TimeoutException: Si el elemento no está listo para escribir dentro del tiempo límite.
        """
        try:
            self.logger.info(f"Esperando a que el elemento con {by}='{locator}' esté listo para escribir.")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                EC.element_to_be_clickable((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(
                f"El elemento con {by}='{locator}' no estuvo listo para escribir después de {self.explicit_wait} segundos."
            )

    def wait_for_element_present(self, by, locator):
        """
        Espera a que un elemento esté presente en el DOM.
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :return: WebElement encontrado.
        :raises TimeoutException: Si el elemento no está presente dentro del tiempo límite.
        """
        try:
            self.logger.info(f"Esperando a que el elemento con {by}='{locator}' esté presente en el DOM.")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_element_located((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(
                f"El elemento con {by}='{locator}' no estuvo presente en el DOM después de {self.explicit_wait} segundos."
            )

    def wait_for_element_absent(self, by, locator):
        """
        Espera a que un elemento no esté presente en el DOM.
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :return: True si el elemento no está presente, de lo contrario TimeoutException.
        """
        try:
            self.logger.info(f"Esperando a que el elemento con {by}='{locator}' no esté presente en el DOM.")
            return WebDriverWait(self.driver, self.explicit_wait).until_not(
                EC.presence_of_element_located((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(
                f"El elemento con {by}='{locator}' aún está presente en el DOM después de {self.explicit_wait} segundos."
            )

    def wait_for_element_exists(self, by, locator):
        """
        Espera a que un elemento exista en el DOM.
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :return: True si el elemento existe, de lo contrario TimeoutException.
        """
        try:
            self.logger.info(f"Esperando a que el elemento con {by}='{locator}' exista en el DOM.")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_element_located((by, locator))
            )
        except:
            return False

    def wait_for_text_in_element(self, by, locator, text):
        """
        Espera a que un elemento contenga un texto específico.
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :param text: Texto esperado en el elemento.
        :return: True si el texto está presente, de lo contrario TimeoutException.
        """
        try:
            self.logger.info(f"Esperando a que el elemento con {by}='{locator}' contenga el texto '{text}'.")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                EC.text_to_be_present_in_element((by, locator), text)
            )
        except TimeoutException:
            raise TimeoutException(
                f"El texto '{text}' no se encontró en el elemento con {by}='{locator}' después de {self.explicit_wait} segundos."
            )

    def wait_for_text_in_element_value(self, by, locator, text):
        """
        Espera a que un elemento contenga un texto específico en su atributo value.
        :param by: Método de búsqueda (e.g., By.ID, By.XPATH).
        :param locator: Ubicación del elemento.
        :param text: Texto esperado en el atributo value del elemento.
        :return: True si el texto está presente, de lo contrario TimeoutException.
        """
        try:
            self.logger.info(f"Esperando a que el atributo value del elemento con {by}='{locator}' contenga el texto '{text}'.")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                EC.text_to_be_present_in_element_value((by, locator), text)
            )
        except TimeoutException:
            raise TimeoutException(
                f"El texto '{text}' no se encontró en el atributo value del elemento con {by}='{locator}' después de {self.explicit_wait} segundos."
            )

    def wait_for_element_not_visible(self, by, locator):
        """Espera a que un elemento ya no sea visible."""
        try:
            self.logger.info(f"Esperando a que el elemento con {by}='{locator}' ya no sea visible.")
            return WebDriverWait(self.driver, self.explicit_wait).until_not(
                EC.visibility_of_element_located((by, locator))
            )
        except TimeoutException:
            raise TimeoutException(
                f"El elemento con {by}='{locator}' aún es visible después de {self.explicit_wait} segundos."
            )

    def wait_for_attribute(self, by, locator, attribute, value):
        """Espera a que un elemento tenga un atributo con un valor específico."""
        try:
            self.logger.info(f"Esperando a que el atributo '{attribute}' del elemento con {by}='{locator}' contenga el valor '{value}'.")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                EC.element_attribute_to_include((by, locator), attribute, value)
            )
        except TimeoutException:
            raise TimeoutException(
                f"El atributo '{attribute}' del elemento con {by}='{locator}' no contiene el valor '{value}' después de {self.explicit_wait} segundos."
            )

    def wait_for_alert_present(self):
        """Espera a que un alert esté presente."""
        try:
            self.logger.info("Esperando a que un alert esté presente.")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                EC.alert_is_present()
            )
        except TimeoutException:
            raise TimeoutException(
                f"El alert no estuvo presente después de {self.explicit_wait} segundos."
            )

    def wait_for_file_download(self, filename):
        """Espera hasta que un archivo se haya descargado."""
        try:
            self.logger.info(f"Esperando a que el archivo '{filename}' se descargue.")
            base_dir = os.path.dirname(os.path.abspath(__file__))
            download_dir = os.path.join(base_dir, "../drivers/downloads")
            return WebDriverWait(self.driver, self.explicit_wait).until(
                FileDownloaded(os.path.join(self.get_download_directory(), filename), self.logger)
            )
        except TimeoutException:
            raise TimeoutException(f"El archivo '{filename}' no se descargó después de {self.explicit_wait} segundos.")

    def get_download_directory(self):
        """Obtiene el directorio de descargas del navegador."""
        try:
            self.logger.info("Obteniendo el directorio de descargas del navegador.")
            base_dir = os.path.dirname(os.path.abspath(__file__))
            download_dir = os.path.join(base_dir, "../drivers/downloads")
            return download_dir
        except:
            raise Exception("No se pudo obtener el directorio de descargas del navegador.")

    def file_exists(self, download_dir, filename):
        """Espera hasta que un archivo exista en un directorio."""
        try:
            self.logger.info(f"Esperando a que el archivo '{filename}' exista.")
            # base_dir = os.path.dirname(os.path.abspath(__file__))
            # download_dir = os.path.join(base_dir, "../drivers/downloads")
            directory = download_dir
            # files = os.listdir(directory)
            # return filename in files
            self.logger.info(f"Directorio: {directory}")
            self.logger.info(f"Archivos: {os.listdir(directory)}")
            for i in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, i)) and filename in i:
                    return True
            return False
            # return [entry for entry in os.listdir(directory) if entry.startswith(filename) and os.path.exists(entry)]
        except:
            raise Exception(f"El archivo '{filename}' no existe en el directorio.")

    def remove_downloads(self):
        """Elimina todos los archivos descargados en la carpeta de descargas."""
        try:
            self.logger.info("Eliminando todos los archivos descargados.")
            base_dir = os.path.dirname(os.path.abspath(__file__))
            download_dir = os.path.join(base_dir, "../drivers/downloads")
            files = os.listdir(download_dir)
            for file in files:
                os.remove(os.path.join(download_dir, file))
            print("Archivos descargados eliminados.")
        except:
            raise Exception("No se pudieron eliminar los archivos descargados.")

    def set_implicit_wait(self, timeout=None):
        """
        Configura una espera implícita para el WebDriver.
        :param timeout: Tiempo en segundos para la espera implícita (por defecto, usa el timeout inicial).
        """
        try:
            self.logger.info(f"Configurando una espera implícita a {timeout} segundos.")
            wait_time = timeout if timeout is not None else self.implicitly_wait
            self.driver.implicitly_wait(wait_time)
            print(f"Espera implícita configurada a {wait_time} segundos.")
        except:
            raise Exception("No se pudo configurar la espera implícita.")

    def reset_implicit_wait(self):
        """Restablece la espera implícita del WebDriver al valor predeterminado."""
        try:
            self.logger.info(f"Restableciendo la espera implícita a {self.implicitly_wait} segundos.")
            self.driver.implicitly_wait(self.implicitly_wait)
            print(f"Espera implícita restablecida a {self.implicitly_wait} segundos.")
        except:
            raise Exception("No se pudo restablecer la espera implícita.")

    def wait_for_page_load(self, timeout=None):
        """
        Espera a que la página esté completamente cargada.
        :param timeout: Tiempo en segundos para la espera (por defecto, usa el timeout inicial).
        """
        try:
            self.logger.info("Esperando a que la página esté completamente cargada.")
            wait_time = timeout if timeout is not None else self.explicit_wait
            WebDriverWait(self.driver, wait_time).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            print("Página completamente cargada.")
        except TimeoutException:
            raise TimeoutException(f"La página no se cargó completamente después de {wait_time} segundos.")

    def set_explicit_wait(self, timeout):
        """
        Configura un tiempo de espera explícita.
        :param timeout: Tiempo en segundos para la espera explícita.
        """
        try:
            self.logger.info(f"Configurando una espera explícita a {timeout} segundos.")
            self.explicit_wait = timeout
            print(f"Espera explícita configurada a {timeout} segundos.")
        except:
            raise Exception("No se pudo configurar la espera explícita.")


class FileDownloaded:
    def __init__(self, file_path, logger):
        self.logger = logger
        self.file_path = file_path

    def __call__(self, driver):
        try:
            self.logger.info(f"Esperando a que el archivo '{self.file_path}' exista.")
            directory = self.file_path
            self.logger.info(f"Directorio: {directory}")
            self.logger.info(f"Archivos: {os.listdir(directory)}")
            for i in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, i)) and self.file_path in i:
                    return os.path.isfile(os.path.join(directory, i))
            return False
            # return [entry for entry in os.listdir(directory) if entry.startswith(filename) and os.path.exists(entry)]
        except:
            raise Exception(f"El archivo '{self.file_path}' no existe en el directorio.")
