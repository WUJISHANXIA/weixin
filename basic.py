# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests


class Basic(object):
    def __init__(self):
        self.__access_token = ''
        self.__left_time = 0
    def __real_get_access_token(self):
        app_id = 'XXX'   #put your weixin app_id here
        app_secret = 'XXX'  #put your weixin app_secret here
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(app_id,app_secret)
        response = requests.get(url = url)
        data = json.loads(response.content)
        self.__access_token = data['access_token']
        self.__left_time = data['expires_in']
        #print data['access_token']
        #print data['expires_in']
    def get_access_token(self):
        return self.__real_get_access_token()
if __name__ == '__main__':
    Basic().get_access_token()