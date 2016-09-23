"""Selenium test voor de app kalenders."""
# standard python imports
# third party imports
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# local imports

URL = "http://localhost:8000/kalenders"
FIREFOX_PATH = "/Applications/Firefox46.app/Contents/MacOS/firefox"


class TestSeleniumKalenders(object):
    """webdriver test voor de app kalenders."""

    @pytest.fixture
    def driver(self, request):
        """webdriver opzetten voor Safari."""
        driver = webdriver.Firefox(firefox_binary=FirefoxBinary(FIREFOX_PATH))
        driver.implicitly_wait(10)

        def driver_quit():
            driver.quit()
        request.addfinalizer(driver_quit)
        return driver

    def test_kalenders(self, driver):
        """webdriver test."""
        response = driver.get(URL)
        assert "kalenders" in response
