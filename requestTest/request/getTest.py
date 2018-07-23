#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao
import requests
import json

url = 'http://ktestapi.zhangguishangcheng.com//User/CheckLogin'

'''
request接口自动化get请求练习


s = requests.get(url)
#获取请求的url
print(s.url)
#获取请求是否OK
print(s.ok)
#获取请求协议状态码是否200
print(s.status_code)
#获取请求内容
print(s.text)
#查看requets库都提供了哪些方法
print(dir(s))

'''

'''
post请求，json格式参数处理练习

headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
           'Origin':'http://ktest.zhangguishangcheng.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
           'Content-Type':'application/x-www-form-urlencoded',
           'Referer':'http://ktest.zhangguishangcheng.com/Home/Login',
           'Pragma':'no-cache',
           'Cache-Control':'no-cache',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.9',
           'Host':'ktestapi.zhangguishangcheng.com',
           'X-KMS-AuthToken':'null'}

data = {'txtLoginName':'15908168410','txt_Password':'q11111','devKey':'623f2ecf-0e3a-4e7f-8ef4-f8387cb55153'}

r = requests.post(url,headers=headers,data=data)
#断言返回业务状态码status是否为true
print(r.json()['Status'])
print(r.ok)
print(r.url)
print(r.status_code)
print(type(r))
# import json
# dict1 = json.load(r.text)
# print(type(dict1))
'''
'''
post请求
'''
headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
           'Origin':'http://ktest.zhangguishangcheng.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
           'Content-Type':'application/x-www-form-urlencoded',
           'Referer':'http://ktest.zhangguishangcheng.com/Home/Login',
           'Pragma':'no-cache',
           'Cache-Control':'no-cache',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.9',
           'Host':'ktestapi.zhangguishangcheng.com',
           'X-KMS-AuthToken':'null'}

data = {'txtLoginName':'15908168410','txt_Password':'q11111','devKey':'623f2ecf-0e3a-4e7f-8ef4-f8387cb55153'}
#timeout,最大响应时间
r1 = requests.post(url,headers=headers,data=data,timeout=10)

s = r1.text
s1 = r1.json()
print(s)
print(s1)
#对返回text内容进行反序列化
dict1 = json.loads(r1.text)
print(type(dict1))
#断言返回业务状态码是否为true
print(dict1['Status'])
#断言返回ResponseCode是否为0
print(dict1['ResponseCode'])
print(r1.json()['Message'])
print(r1.json()['Data']['authToken'])


