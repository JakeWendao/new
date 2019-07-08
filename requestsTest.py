#!/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao

import requests
import json
data2 = {'email':'liujingjieyear@163.com','icode':'','origURL':'http://www.renren.com/home','domain':'renren.com','key_id':'1','captcha_type':'web_login',
         'password':'a63d66c01f190c64350e606173e0ff655972db4a16e12ef47dbeac1ec1cf1536','rkey':'45719fa80a9cb78dc16c3a4e87b896e9','f':''}

r = requests.post('http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019611953216',data=data2)

print u'请求地址'+' ok ',r.url
dic = json.loads(r.text.encode(r.encoding).decode(r.apparent_encoding))
print dic
print dic['failDescription']