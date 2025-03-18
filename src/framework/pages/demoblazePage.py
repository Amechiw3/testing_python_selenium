
from adapters.selenium_adapter import SeleniumAdapter as UIAdapter
from framework.ports.ui_port import UIPort


class demoblazePage:
    """Página de la tienda en línea Demoblaze."""

    def __init__(self, ui_adapter: UIAdapter, test_config):
        self.ui_adapter = ui_adapter
        self.test_config = test_config
        self.logger = test_config.logger
        self.ui_adapter.configure_logger(self.logger)

    def go_to_page(self):
        """Abre la página de la tienda en línea Demoblaze."""
        self.ui_adapter.navigate(self.ui_adapter.config.get('base_url'))
        self.logger.info(f"Opening the page: {self.ui_adapter.config.get('base_url')}")
        self.ui_adapter.wait_manager.wait_for_page_load()

    def file_exists(self, file_path):
        """Verifica si un archivo existe."""
        assert self.ui_adapter.wait_manager.file_exists(file_path)
        self.ui_adapter.wait_manager.remove_downloads()
