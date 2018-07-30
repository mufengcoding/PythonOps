import http
from urllib import parse,request
from http import cookiejar

from bs4 import BeautifulSoup
import json

#创建cookie处理器
cookiejar = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookiejar), request.HTTPHandler)
request.install_opener(opener)
textmod={"nameOrEmail":"mufengs","userPassword":"57b8f8d4baaa7c8e1c1820f4b58b5025","rememberLogin":"true","captcha":""}
#json串数据使用
textmod = json.dumps(textmod).encode(encoding='utf-8')
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
url='https://hacpai.com/login'
req = request.Request(url=url,data=textmod,headers=header_dict)
res = request.urlopen(req)
res = res.read()
print(res)
#输出内容:b'{"jsonrpc":"2.0","result":"37d991fd583e91a0cfae6142d8d59d7e","id":1}'
print(res.decode(encoding='utf-8'))
#输出内容:{"jsonrpc":"2.0","result":"37d991fd583e91a0cfae6142d8d59d7e","id":1}

#
# 领取今日积分
# https://hacpai.com/activity/daily-checkin


#输出内容:user=admin&password=admin
#header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url1='https://hacpai.com/activity/daily-checkin'
req1 = request.Request(url=url1,headers=header_dict)
res1 = request.urlopen(req1)
res1 = res1.read()
# print(res1)
#输出内容(python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码):b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'
#print(res1.decode(encoding='utf-8'))
#输出内容:登录成功
html=BeautifulSoup(res1,'html.parser')
c=html.find_all('div','fn-flex points__item')
print(c)
#
# 领取昨日积分
# https://hacpai.com/activity/daily-checkin
print('*'*200)
print('*'*200)
#输出内容:user=admin&password=admin
#header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
url2='https://hacpai.com/activity/yesterday-liveness-reward'
req2 = request.Request(url=url2,headers=header_dict)
res2 = request.urlopen(req2)
res2 = res2.read()
html=BeautifulSoup(res2,'html.parser')
c1=html.find_all('div','fn-flex points__item')
print(c1)
#print(res2)
#输出内容(python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码):b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'
#print(res2.decode(encoding='utf-8'))
#输出内容:登录成功