from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils
from pages.base_page import BasePage

class GooglePage(BasePage):
    TEXTAREA_SEARCH = (By.CLASS_NAME, "gLFyf")
    LOGIN_BUTTON = (By.CLASS_NAME, "gNO89b")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)  # Inicializar utilidades de espera
    

    def search(self, busqueda):
        self.send_keys(self.TEXTAREA_SEARCH, busqueda)
        self.click(self.LOGIN_BUTTON)
