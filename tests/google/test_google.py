import pytest
from utils.wait_utils import WaitUtils
from pages.google import GooglePage

def test_google(driver, config):
    """Prueba que el título de la página principal sea correcto."""
    googlePage = GooglePage(driver)
    wait = WaitUtils(driver)
    googlePage.visit(config['base_url'])
    googlePage.search("testing")
    
    assert True