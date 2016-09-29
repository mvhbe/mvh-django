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
    def browser(self, request):
        """webdriver opzetten voor Safari."""
        browser = webdriver.Firefox(firefox_binary=FirefoxBinary(FIREFOX_PATH))
        browser.implicitly_wait(10)

        def browser_quit():
            browser.quit()
        request.addfinalizer(browser_quit)
        return browser

    def test_kalenders(self, browser):
        """webdriver test."""
        response = browser.get(URL)
        print("response = ", response)
        assert "kalenders" in response.body
