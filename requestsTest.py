#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

import requests
r = requests.get('http://www.baidu.com')
print r.text
print u'请求地址'+' ok ',r.url
print r.status_code
print r.json()   #这个地方报错是正常的，因为返回的信息不是json编码