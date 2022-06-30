from selene.support.shared import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def before_each():
    browser.open('https://google.com')
    browser.driver.maximize_window()
    browser.config.hold_browser_open = True

