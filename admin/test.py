# -*- coding: utf-8 -*-

from AdminClient import AdminClient

if __name__ == '__main__':

    admin = AdminClient(url="http://localhost:8080",
     token="access_token")

    json = '{\
    "name":"Fess : https://fess.codelibs.org/",\
    "description":"Enterprise Search Server: Fess",\
    "urls":"https://fess.codelibs.org/",\
    "included_urls":"https://fess.codelibs.org/.*",\
    "user_agent":"Mozilla/5.0",\
    "num_of_thread":1,\
    "interval_time":10000,\
    "boost":1.0,\
    "available":true,\
    "sort_order":0\
    }'

    admin.createWebconfig(data=json)
