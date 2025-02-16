from utils.logger import setup_logger
from utils.wait_utils import WaitUtils
from pages.base_page import BasePage


class demoblazePage(BasePage):
    """Página de la tienda en línea Demoblaze."""

    def __init__(
        self, driver, config, logger_name, screenshotDIR, log_DIR, testName=""
    ):
        self.driver = driver
        self.config = config
        self.logger_name = logger_name
        self.screenshotDIR = screenshotDIR
        self.log_DIR = log_DIR
        self.testName = testName

        self.logger = setup_logger(logger_name, log_DIR)
        self.wait = WaitUtils(driver, config)

    def go_to_page(self):
        self.navigate(self.config["base_url"])
        self.logger.info(f"Opening the page: {self.config['base_url']}")
        self.wait.wait_for_page_load()
