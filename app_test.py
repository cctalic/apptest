import time
from appium import webdriver

capabilities = {}
# Android平台测试
capabilities['platformName'] = 'Android'
# 测试手机版本为5.0
capabilities['platformVersion'] = '5.1.1'
capabilities['deviceName'] = 'Android Emulator'
# 系统手机中的联系人app的包名
capabilities['appPackage'] = 'com.android.contacts'
# 系统手机中的联系人app的主入口activity
capabilities['appActivity'] = '.activities.PeopleActivity'
capabilities['unicodeKeyboard'] = 'True'
capabilities['resetKeyboard'] = 'True'
# 连接测试机所在服务器
driver = webdriver.Remote('http://127.0.0.1:5037/wd/hub', capabilities)

try:
# com.android.contacts:id/floating_action_button为通过uiautomatorviewer截取联系人界面获取到的
    element = driver.find_element_by_id('com.android.contacts:id/floating_action_button')
    #如果找到该id所指定控件，则进行点击操作
    element.click()
except:
    print("exist")
    pass

time.sleep(2)
#断开连接
driver.quit()
