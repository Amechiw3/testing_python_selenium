from utils.logger import setup_logger
from utils.wait_utils import WaitUtils
from pages.base_page import BasePage


class demoblazePage(BasePage):
    """Página de la tienda en línea Demoblaze."""

    def __init__(
        self, driver, config, logger_name, screenshot_dir, log_dir, testName=""
    ):
        self.driver = driver
        self.config = config
        self.logger_name = logger_name
        self.screenshot_dir = screenshot_dir
        self.log_dir = log_dir
        self.test_name = testName

        self.logger = setup_logger(logger_name, log_dir)
        self.wait = WaitUtils(driver, config)

    def go_to_page(self):
        """Abre la página de la tienda en línea Demoblaze."""
        self.navigate(self.config["base_url"])
        self.logger.info(f"Opening the page: {self.config['base_url']}")
        self.wait.wait_for_page_load()
