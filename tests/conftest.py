import pytest
import os
from selenium import webdriver
from tests import config

def pytest_addoption(parser):
    # parser.addoption方法支持baseurl的参数配置
    parser.addoption("--baseurl",
                     action="store",
                     default="https://passport.baidu.com/d",
                     help="base URL for the application under test")
    parser.addoption("--browser",
                     action="store",
                     default="firefox",
                     help="the browser name that your want to test")

@pytest.fixture()
def driver(request):
    # 通过config.getoption方法读取baseurl配置，并传给config.baseurl参数
    config.base_url = request.config.getoption("--baseurl")
    # 通过config.getoption方法读取browser配置，并传给config.browser参数
    config.browser = request.config.getoption("--browser").lower()
    if config.browser == 'firefox':
        # 命令行pytest --browser=firefox
        _gecko_driver = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'drivers', 'geckodriver.exe')
        # 创建Firefox的driver对象，exc..path为driver的物理地址
        driver_ = webdriver.Firefox(executable_path=_gecko_driver)
    elif config.browser == 'chrome':
        _chrome_driver = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'drivers', 'chromedriver.exe')
        # 创建Chrome的driver对象，exc..path为driver的物理地址
        driver_ = webdriver.Firefox(executable_path=_chrome_driver)

    def quit():
        driver_.quit()

    request.addfinalizer(quit)  # 每个测试方法执行完毕后，会执行quit方法（即退出selenium），完成了一个setup和teardown操作
    return driver_