# -*- coding: utf-8 -*-

import requests
import json

class AdminClient(object):

    def __init__(self, url, token):
        self.headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/x-www-form-urlencoded'}
        self.url = url.__add__('/api/admin')

    def createWebconfig(self, data):
        requestUrl = self.url.__add__('/webconfig/setting')
        print("requestUrl = " + requestUrl)
        print("data = " + data)
        response = requests.put(url=requestUrl,data=data,headers=self.headers)
        print(response.status_code)
        print(response.text)