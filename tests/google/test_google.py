from datetime import datetime
import time
import pytest
from utils.wait_utils import WaitUtils
from pages.google import GooglePage

@pytest.mark.google
class TestGoogle:
    log_name = "TestGoogle_Logger"
    log_date = datetime.now().date()
    log_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    screenshotDIR = f"google/google_{log_date}/google_{log_datetime}"
    log_DIR = f"google/google_{log_date}/google_{log_datetime}"


    def test01_google(self, driver, config):
        testName = "Test01_Busqueda"
        self.log_name = f"{self.log_name}_{testName}"
        self.screenshotDIR = f"{self.screenshotDIR}/{testName}"
        self.log_DIR = f"{self.log_DIR}/{testName}"

        googlePage = GooglePage(driver, config, self.log_name, self.screenshotDIR, self.log_DIR, testName)
        googlePage.navigate(config['base_url'])
        googlePage.search("testing")
        googlePage.take_screenshot(self.screenshotDIR, "01_Busqueda")
        time.sleep(10)
        
        assert True