from framework.utilities.logger import setup_logger


class Configuration:
    """Clase para almacenar la configuración de la prueba."""
    def __init__(self, config, screenshot_dir, logger_name, logger_dir, test_name=""):
        self.config = config
        self.screenshot_dir = screenshot_dir
        self.logger_name = logger_name
        self.logger_dir = logger_dir
        self.test_name = test_name
        self.logger = setup_logger(self.logger_name, self.logger_dir)