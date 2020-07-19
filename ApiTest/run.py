import unittest
import os
import time
from ApiTest import HTMLTestRunner

def html_report_folder_path(folder_name):
    _current_folder_path = os.getcwd()
    # 定义Html报告文件夹地址
    _html_report_folder_path = _current_folder_path + '\\' + folder_name
    is_folder_existed = os.path.exists(_html_report_folder_path)
    # 判断html报告文件夹是否存在，存在则提示并返回文件夹地址，不存在则创建文件夹并返回文件夹地址
    if is_folder_existed:
        print("html存放路径{0}已存在:".format(_html_report_folder_path))
        return _html_report_folder_path
    else:
        print("HtmlReport存放路径{0}不存在,系统将为你自动创建:".format(_html_report_folder_path))
        os.makedirs(_html_report_folder_path)
        return _html_report_folder_path

def test_cases_set():
    # 定义unittest测试套件对象
    test_suites = unittest.TestSuite()
    from ApiTest import python_api_test_automation
    # 将测试内容加入测试套件，并返回
    test_suites.addTest(unittest.TestLoader().loadTestsFromTestCase(python_api_test_automation.CNodeApiTet))
    return test_suites

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%dT&H-%m-%s", time.localtime(time.time()))
    print("时间戳是:{0}".format(now))
    # Html文件夹地址
    _folder_path = html_report_folder_path(folder_name='HTMLTestReports自动化测试报告中心')
    # 生成Html报告的文件名
    _html_report_file_abspath = os.path.join(_folder_path, u'接口API自动化测试报告_' + now + '.html')
    fp = open(_html_report_file_abspath, 'wb')
    # 实例化HtmlTestRunner类，执行测试套件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           verbosity=2,
                                           title='接口API自动化测试报告 -- 测试结果展示',
                                           description='测试用例执行情况入如下：')
    runner.run(test_cases_set())
    fp.close()