from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils
from pages.base_page import BasePage

class GooglePage(BasePage):
    TEXTAREA_SEARCH = (By.XPATH, "//textarea[@class='gLFyf']")
    LOGIN_BUTTON = (By.XPATH, "//input[@class='gNO89b']")

    def __init__(self, driver, config, logger_name, screenshotDIR, log_DIR, testName = ""):
        self.driver = driver
        self.config = config
        self.logger_name = logger_name
        self.screenshotDIR = screenshotDIR
        self.log_DIR = log_DIR
        self.testName = testName
    
    def goto(self):
        self.navigate(self.config['base_url'])
    
    def search(self, busqueda):
        self.send_keys(self.TEXTAREA_SEARCH, busqueda)
        self.click(self.LOGIN_BUTTON)
