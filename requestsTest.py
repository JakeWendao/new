#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

import requests
data = {'word':'Selenium自动化测试实战（Python语言版）'}

r = requests.get('https://yuedu.baidu.com/search',params=data)
# r.encoding= 'iso8859-1'
print u'请求地址'+' ok ',r.url

print type(r)

print r.text
print r.json()
print (r.text.encode(r.encoding).decode(r.apparent_encoding))
