from selene.support.shared import browser
import pytest
import config

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = config.settings.timeout
    browser.config.base_url = "https://my.exness.com"
    browser.config.hold_browser_open = True

    yield

#    browser.quit()

