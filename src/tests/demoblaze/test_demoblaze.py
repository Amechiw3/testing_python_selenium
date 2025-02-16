import time
import pytest
import unittest
from datetime import datetime
from pages.demoblazePage import demoblazePage


@pytest.mark.blaze
class TestDemoblaze(unittest.TestCase):
    log_name = "TestDemoblaze_Logger"
    log_date = datetime.now().date()
    log_datetime = datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    screenshotDIR = f"Demoblaze/Demoblaze_{log_date}/Demoblaze_{log_datetime}"
    log_DIR = f"Demoblaze/Demoblaze_{log_date}/Demoblaze_{log_datetime}"

    def test01_Go_To_Page(self, driver, config):
        testName = "Test01_Go_To_PAGE"
        self.log_name = f"{self.log_name}_{testName}"
        self.screenshotDIR = f"{self.screenshotDIR}/{testName}"
        self.log_DIR = f"{self.log_DIR}/{testName}"

        demoblaze = demoblazePage(
            driver, config, self.log_name, self.screenshotDIR, self.log_DIR, testName
        )
        demoblaze.go_to_page()
        time.sleep(10)
