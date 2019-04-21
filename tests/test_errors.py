import pytest
import os
import time
import logging
LOGGER = logging.getLogger(__name__)

def test_404(driver):
    """
    validate that 404 errors are caught in logs
    :return: None
    """
    path = f"file:{os.getcwd()}/test_data/network404.html"
    driver.get(path)
    browser = driver.get_log('browser')
    d = driver.get_log('driver')
    logger = [
        {
            'timestamp': int(round(time.time() * 1000)),
            'url': driver.current_url,
        }
    ]
    for b_log in browser:
        if b_log['level'] == 'SEVERE':
            LOGGER.info(b_log)
            for page in logger:
                LOGGER.info((b_log['timestamp'] - page['timestamp']))
    for log in d:
        LOGGER.info(log)
# https://httpbin.org/

