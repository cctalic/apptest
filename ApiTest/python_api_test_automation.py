import unittest, pytest
from ddt import ddt, data, unpack
import requests
from ApiTest import public_func
from ApiTest import HTMLTestRunner


access_token = '30274f21-9dba-4b70-92ea-bc129a57c981'
base_url = 'https://cnodejs.org/api/v1'

# 引入数据驱动测试，需先引用ddt；
# @ddt
# class CNodeApiTet(unittest.TestCase):
#     def setUp(self):
#         # 验证标志位，后续执行各个test方法时，如果有失败情况，会把这个语句标记为False
#         self._assert_flag = True
#
#     def tearDown(self):
#         pass


def api_new(self, access_token, title, tab, content):
    _pay_load = {'access_token': access_token,
                 'title': title,
                 'tab': tab,
                 'content': content}

    topics_create_a_topic = public_func.HttpRequest('/topics')
    _response = topics_create_a_topic.post(_pay_load)
    print('响应报文是；', _response)

    _success = _response['success']
    print(u'响应结果是：', _success)

    _topic_id = _response['topic_id']
    print(u'响应结果"topic_id":', _topic_id)
    return _success, _topic_id

def api_detail(self, topic_id, mdrender, access_token):
    _payload = {'mdrender': mdrender,
                'accesstoken': access_token}
    topics_topic_details = public_func.HttpRequest('/topic' + '/' + topic_id)
    _response = topics_topic_details.get(_payload)
    print(u'响应报文：', _response)

    _success = _response['success']
    print(u'响应结果success\：', _success)
    _data_json_dict = _response['data']
    print(u'响应结果data：', _data_json_dict)
    _topic_id = _data_json_dict['id']
    print(u'响应结果id：',_topic_id)
    _title = _data_json_dict['title']
    print(u'响应结果title：', _title)
    _tab = _data_json_dict['tab']
    print(u'响应结果tab：', _tab)
    _content = _data_json_dict['conetent']
    print(u'响应结果content：', _content)

    _content_without_html_label = public_func.public_function.wipe_off_html_labels(_content)
    return _success, _topic_id, _title, _tab, _content_without_html_label

def test_api_www6(self, api_name, value):
    _pay_load = {'value': value}
    # http请求接口名称
    _api_test = public_func.HttpRequest(api_name)
    # http请求数据
    _response = _api_test.get(value)
    print(_response)
    return _response


#
# @data([1, 'ask', 5, 'true'],
#       [1, 'ask', 5, 'true'],
#       [1, 'ask', 5, 'true'])
# @unpack
# def test_www6(self, ddt_page, ddt_tab, ddt_limit, ddt_mdrender):
#     print('-----执行test测试方法并读取ddt-----')
#     _page = ddt_page
#     _tab = ddt_tab
#     _limit = ddt_limit
#     _mdrender = ddt_mdrender
#     print('---测试数据是:{0}-{1}-(2}-{3}:'.format(_page, _tab, _limit, _mdrender))

if __name__ == '__main__':
    pytest.main("-s python_api_test_automations.py")
    # test_api_www6
    # fp = open(r'D:\work\python\AppTest\ApiTest\123.html', 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                        verbosity=2,
    #                                        title='接口API自动化测试报告 -- 测试结果展示',
    #                                        description='测试用例执行情况入如下：')
    # test_suite = unittest.TestSuite()
    # test_suite.addTest("")
    # runner.run(123)
    # fp.close()