import pytest
import os
import time


@pytest.mark.usefixtures('driver')
class TestGuineaPig(object):

    def test_404(self, driver):
        """
        validate that 404 errors are caught in logs
        :return: None
        """
        path = f"file:{os.getcwd()}/test_data/network404.html"
        driver.get(path)
        time.sleep(1)
        perf = driver.get_log('performance')
        browser = driver.get_log('browser')
        d = driver.get_log('driver')
        logger = {'timestamp': time.time(),
                  'url': driver.current_url}
        #for log in perf:
        #    print(log)
#
        #print('___________________________')

        for log in browser:
            print(log)

        #print('___________________________')
#
        #for log in d:
        #    print(log)
        print(logger)


        #https://httpbin.org/