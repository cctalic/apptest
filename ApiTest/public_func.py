import requests
import re
import os
import pickle

class HttpRequest(object):
    def __init__(self, api_name):
        self._host_and_port = 'http://www6.web1800.com/'
        self._api_prefix='web1800/status.asmx/'
        self._api_name = api_name
        self._url = self._host_and_port + self._api_prefix + self._api_name
        print('最终访问URL是：', self._url)

    def get(self, payload):
        _response = requests.get(url=self._url, data=payload)
        return _response.json()

    def post(self, payload):
        _response = requests.post(url=self._url, data=payload)
        return _response.json()


class Public_Func(object):
    def wipe_off_html_labels(self, html_str):
        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', html_str)
        return dd

class analysis_of_cases(object):
    def __init__(self):
        self._file_name = 'caseana.pk'
        self._pickle_file_init(self._file_name)

    def _pickle_file_init(self, file_name):
        if os.path.exists(file_name):
            print('你所设置的文件{0}已存在'.format(file_name))
            pass
        else:
            print('你所设置的文件{0}不存在，系统将自动创建并初始化数据:'.format(file_name))
            _folder_path = os.getcwd()
            _file = _folder_path + '\\' + file_name
            _dict_data = {'已执行测试用例总次数': 0,
                          '测试用例失败总次数': 0}
            with open(_file, 'wb') as f:
                pickle.dump(_dict_data, f)

    def _pickle_serialize(self, file_name, dict_data):
        with open(file_name, 'wb') as f:
            pickle.dump(dict_data, f)

    def _picket_Deserialization(self, file_name):
        with open(file_name, 'rb') as f:
            _dict_data = pickle.load(f)
            return _dict_data

    def case_success_time(self):
        _dict_data = self._picket_Deserialization(self._file_name)
        _dict_data['已执行测试用例总次数'] +=1
        self._pickle_serialize(self._file_name, _dict_data)

    def case_fail_time(self):
        _dict_data = self._picket_Deserialization(self._file_name)
        _dict_data['测试用例失败总数' ] +=1
        self._pickle_serialize(self._file_name, _dict_data)

    def case_execute_count(self):
        _dict_data = self._picket_Deserialization(self._file_name)
        _case_execute_count = _dict_data['case_execute_count']
        return _case_execute_count

    def case_execute_fail_count(self):
        _dict_data = self._picket_Deserialization(self._file_name)
        _case_execute_faile_count = _dict_data['case_execute_fail_count']
        return _case_execute_faile_count


if __name__ == '__main__':
    _html_str = '<div class="markdown-text"><p>哈哈哈哈哈</p>\n</div>'
    public_function = Public_Func()
    # 去除Html标签后的内容
    res = public_function.wipe_off_html_labels(_html_str)
    print('去掉html标签后效果如下: \n{0}'.format(res))

    wechat_dict = {}
    wechat_dict['姓名'] = 'fs'
    wechat_dict['微信号'] = 'autotest_coach'
    wechat_dict['昵称'] ='ronald'
    wechat_dict['型号'] = 'iquicktest'
    print('微信联系方式字典:{0}'.format(wechat_dict))
    r = HttpRequest.get('GetAddressByIp')


