import pytest, requests, json
import logging
from ui import config


class TestAPI():
    _url = config.Api_address()
    _api_name = config.Api_name()

    url = _url[0] + _url[1] + _api_name
    print(url)

if __name__ =='__main__':
    TestAPI()