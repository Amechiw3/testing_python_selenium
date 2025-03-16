import time
import pytest
from datetime import datetime
from framework.pages.demoblazePage import demoblazePage
from framework.utilities.configuration import Configuration


@pytest.mark.blaze
class TestDemoblaze:
    logger_name = "demoblaze_logger"
    logger_date = datetime.now().date()
    logger_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    logger_dir = f"demoblaze/demoblaze_{logger_date}/demoblaze_{logger_datetime}"
    screenshot_dir = f"demoblaze/screenshots/demoblaze_{logger_date}/demoblaze_{logger_datetime}"

    def setup_test(self, test_name):
        self.logger_name = f"{self.logger_name}::{test_name}"
        self.logger_dir = f"{self.logger_dir}/{test_name}"
        self.screenshot_dir = f"{self.screenshot_dir}/{test_name}"
    
    """
    def test01_Go_To_Page(self, ui_adapter):
        test_name = "test01_Go_To_Page"
        self.setup_test(test_name)
        test_config = Configuration(
            config=ui_adapter.config,
            screenshot_dir=self.screenshot_dir,
            logger_name=self.logger_name,
            logger_dir=self.logger_dir,
            test_name=test_name
        )

        demoblaze = demoblazePage(ui_adapter, test_config)
        demoblaze.go_to_page()
        time.sleep(10)
    """
    def test02_File_Exists(self, ui_adapter):
        test_name = "test02_File_Exists"
        self.setup_test(test_name)
        test_config = Configuration(
            config=ui_adapter.config,
            screenshot_dir=self.screenshot_dir,
            logger_name=self.logger_name,
            logger_dir=self.logger_dir,
            test_name=test_name
        )

        demoblaze = demoblazePage(ui_adapter, test_config)
        demoblaze.go_to_page()
        assert demoblaze.file_exists("test-output")
        time.sleep(10)