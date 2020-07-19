from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.taobao.taobao'
desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("delete").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("=").click()

driver.quit()