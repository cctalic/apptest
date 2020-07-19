import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pages import flight_login_page


class TestFlightLogin():

    @pytest.fixture()
    def login(self, driver):
        driver.implicitly_wait(5)
        return flight_login_page.FlightLoginPage(driver)

    @pytest.mark.loginsuccess
    def test_valid_credential(self, login):
        login.login_baidu('cctalic', '123hw321')
        #assert login.success_msg_exist()

    @pytest.mark.loginfail
    def test_invalid_credential(self, login):
        login.login_baidu('cctalic', '123')
        assert login.fail_msg_exist()