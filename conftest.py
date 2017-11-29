import pytest

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.yield_fixture(scope='function')
def driver():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL',
                         'performance': 'ALL',
                         'driver': 'ALL'}
    browser = webdriver.Chrome(desired_capabilities=d)

    yield browser

    try:
        browser.quit()
    except WebDriverException:
        # we can ignore the exceptions of WebDriverException type -> We're done with tests.
        print(
            'Warning: The driver failed to quit properly. Check test and server side logs.')
