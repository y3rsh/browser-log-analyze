import pytest
import os
import time


class TestGuineaPig():

    def test_404(self, selenium):
        """
        validate that 404 errors are caught in logs
        :return: None
        """
        path = f"file:{os.getcwd()}/test_data/network404.html"
        selenium.get(path)
        browser = selenium.get_log('browser')
        d = selenium.get_log('driver')
        logger = [
            {
                'timestamp': int(round(time.time() * 1000)),
                'url': selenium.current_url,
            }
        ]
        for log in browser:
            if log['level'] == 'SEVERE':
                print(log)
                for page in logger:
                    print(log['timestamp'] - page['timestamp'])

        for log in d:
            print(log)
# https://httpbin.org/
