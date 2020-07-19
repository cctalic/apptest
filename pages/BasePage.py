from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests import config

#  封装页面对象
class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _goto(self, url):
        # 获取config中的base_url，并加上url地址组成最终url地址
        # base_url类似于http;//127.0.0.1/   url类似于/login
        self.driver.get(config.base_url + url)

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _click(self, locator):
        self._find(locator).click()

    def _input(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _is_displayed(self, locator):
        try:
            self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
        return True

    def _wait_until_displayed(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located(*locator))
        except TimeoutError:
            return False
        return True