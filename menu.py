# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from basic import Basic

class Menu(object):
    def __init__(self):
        pass
    def create(self, post_data, access_token):
        url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}".format(access_token)
        if isinstance(post_data, unicode):
            post_data = post_data.encode('utf-8')
        response = requests.post(url=url, data=post_data)
        print response.text
    def query(self, access_token):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token={0}'.format(access_token)
        response = requests.post(url=url)
        print response.text
    def delete(self, access_token):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token={0}'.format(access_token)
        response = requests.post(url=url)
        print response.text
if __name__ == '__main__':
    menu = Menu()
    post_json = """
    {
        "button":
        [
            {
                "type": "click",
                "name": "开发指引",
                "key":  "mpGuide"
            },
            {
                "name": "公众平台",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "更新公告",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "接口权限说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "返回码说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                    }
                ]
            },
            {
                "type": "media_id",
                "name": "旅行",
                "media_id": "z2zOokJvlzCXXNhSjF46gdx6rSghwX2xOD5GUV9nbX4"
            }
          ]
    }
    """
    access_token = Basic().get_access_token()
    menu.create(post_json, access_token)
