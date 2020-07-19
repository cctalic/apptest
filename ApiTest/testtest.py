import unittest, pytest
from ddt import ddt, data, unpack
import requests
from ApiTest import public_func
from ApiTest import HTMLTestRunner



def api_www6(self, api_name, value):
    _pay_load = {'value': value}
    # http请求接口名称
    _api_test = public_func.HttpRequest(api_name)
    # http请求数据
    _response = _api_test.get(value)
    print(_response)
    return _response

def test_api_www6():
    api_www6('getaddressip', '127.0.0.1')


if __name__ =='__main__':
    pytest.main('-s')


