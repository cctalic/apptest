from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import time

# 封装页面类
class FlightLoginPage(BasePage):
    _usr_textbox = (By.ID,  'TANGRAM__PSP_3__userName')
    _pwd_textbox = (By.ID, 'TANGRAM__PSP_3__password')
    _login_button = (By.ID, 'TANGRAM__PSP_3__submit')

    _login_fail_msg  = (By.ID, "TANGRAM__PSP_3__error")
    _switch_user_pwd_log = (By.ID, 'TANGRAM__PSP_3__footerULoginBtn')

    def __init__(self, driver):
        self.driver = driver
        self._goto('v2/?login')

    def login_baidu(self, usr, pwd):
        # 切换到用户名和密码登录窗口
        self._click(self._switch_user_pwd_log)
        self._input(self._usr_textbox, usr)
        self._input(self._pwd_textbox, pwd)
        self._click(self._login_button)

    def success_msg_exist(self):
        pass
        #return self._is_displayed(self._login_success_msg)

    def fail_msg_exist(self):
        return self._is_displayed(self._login_fail_msg)
