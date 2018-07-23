#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao

import requests
import json
'''
post请求
'''
# url = 'http://ktestapi.zhangguishangcheng.com//User/CheckLogin'
# headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
#            'Origin':'http://ktest.zhangguishangcheng.com',
#            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
#            'Content-Type':'application/x-www-form-urlencoded',
#            'Referer':'http://ktest.zhangguishangcheng.com/Home/Login',
#            'Pragma':'no-cache',
#            'Cache-Control':'no-cache',
#            'Accept-Encoding':'gzip, deflate',
#            'Accept-Language':'zh-CN,zh;q=0.9',
#            'Host':'ktestapi.zhangguishangcheng.com',
#            'X-KMS-AuthToken':'null'}
#
# data = {'txtLoginName':'15908168410','txt_Password':'q11111','devKey':'623f2ecf-0e3a-4e7f-8ef4-f8387cb55153'}
#
# r1 = requests.post(url,headers=headers,data=data)
#
# s = r1.text
# s1 = r1.json()
# print(s)
# print(s1)
# #对返回text内容进行反序列化
#
#
# dict1 = json.loads(r1.text)
# print(type(dict1))
# #断言返回业务状态码是否为true
# print(dict1['Status'])
# #断言返回ResponseCode是否为0
# print(dict1['ResponseCode'])
# print(r1.json()['Message'])
# print(r1.json()['Data']['authToken'])

'''post请求中json参数的运用'''
url1 = 'http://103.6.223.203:8016/User/CheckLogin'
data1 = data = {'txtLoginName':'15908168410','txt_Password':'q11111','devKey':'16acc8c6-00d7-47f8-955c-8682a3fb5c08'}
r2 = requests.post(url1,data=data1)
print(r2.text)



'''post请求中对json参数的处理'''
hearders = {'Origin':'http://103.6.223.203:8015',
            'Referer':'http://103.6.223.203:8015/Goods/Edit?id=2501&noSpecEdit=1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
            'Content-Type':'application/json',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'X-KMS-AuthToken':'rPjK9e32TGmTP5Q6QvkygULceKPwRG5XkbQcu+62ithh0cVHqmknxQWQZrPkGToZ3mzxnhWj07rF5I0QOmMvg+tBBSxrgXMaXx3Jv3eGOFgmKc6Ur6vkW9wXQPUu0PK44/cTGNuKrT6ob29uI6NEcPRD47dZpcY1jixdH9UQtoVeYiW8qdKyJdwrgH+gZX5P9xTEW1h0IMM0q+LLAc/tlclaC/ciW1JJDzcm3tbwnMVYblt/A5J6xxkcBZKIxeCFFfZr11fZFvKk/BZO5prUQ9xa69j+VqYJOsNyHy59/sd8nhIsaeW3f67WMCfDeFYGPFrt/AJCxIBSeBeeIi8JyZvI/lA+LypA9cATREN2dR6H0EkJx8QTl8LxN0AIDievACX5OR9oOh3ZxhVyw8nG4/xEwQS0fgPW',
            'X-KMS-DevKey':'16acc8c6-00d7-47f8-955c-8682a3fb5c08',
            }
data = {
	"SPU": {
		"Specifications":'null',
		"SpecOptIDs": 'null',
		"CommodityID": 2501,
		"IsShow": 'false',
		"Weight": 1,
		"Length": 0,
		"Thumb":'null',
		"Width": 0,
		"Height": 0,
		"SkuKey": "20180722214715021",
		"BarCode": "20180722214715001",
		"DefaultRecommendSalePrice": 0,
		"DefaultPurchasingPrice": 1,
		"DefaultMarketPrice": 1,
		"NatureValue":'null',
		"IsInUse": 'false',
		"CommodityName": "aaa",
		"Property": "a",
		"IsUpShelf": 'false',
		"Status":'true',
		"CategoryID": 1118,
		"BrandID": 148,
		"HsCode":'null',
		"CreateOperator": 313,
		"CategoryName": "ddd",
		"BrandName": "ddd",
		"DealerName":'null',
		"CreateDate": "2018-07-22 22:39:22",
		"UpdateDate": "2018-07-22 22:39:22",
		"Notes":'null',
		"Detail":'null',
		"SPUID": 1595451485,
		"UpdateOperator": 313,
		"DealerID": 140,
		"Sort": 999,
		"UnitID": 242,
		"TagWord": "a",
		"UnitName": "ddd",
		"DealerNo":'null'
	},
	"SKUs": [{
		"Specifications":'null',
		"SpecOptIDs":'null',
		"CommodityID": 2501,
		"IsShow": 'false',
		"Weight": 1,
		"Length": 0,
		"Thumb":'null',
		"Width": 0,
		"Height": 0,
		"SkuKey": "20180722214715001",
		"BarCode": "20180722214715001",
		"DefaultRecommendSalePrice": 0,
		"DefaultPurchasingPrice": 1,
		"DefaultMarketPrice": 1,
		"NatureValue":'null',
		"IsInUse": 'false',
		"CommodityName": "aaa",
		"Property": "a",
		"IsUpShelf": 'false',
		"Status": 'true',
		"CategoryID": 1118,
		"BrandID": 148,
		"HsCode":'null',
		"CreateOperator": 313,
		"CategoryName": "ddd",
		"BrandName": "ddd",
		"DealerName":'null',
		"CreateDate": "2018-07-22 22:39:22",
		"UpdateDate": "2018-07-22 22:39:22",
		"Notes":'null',
		"Detail":'null',
		"SPUID": 1595451485,
		"UpdateOperator": 313,
		"DealerID": 140,
		"Sort": 999,
		"UnitID": 242,
		"TagWord": "a",
		"UnitName": "ddd",
		"DealerNo": 'null'
	}],
	"Material": {
		"CommodityID": 2501,
		"SkuKey": "20180722214715001",
		"RollingPhotos": "",
		"Context": "",
		"RecommendText": "",
		"UpdateTime": "2018-07-22 22:39:22",
		"Thumbnail": 'null',
		"RollingPicturesList": []
	},
	"Specifications": [{
		"NatureID": 345,
		"NatureName": "ddd",
		"CategoryID": 1,
		"ShowSort": 1,
		"Status": 'true',
		"Values": 'null'
	}],
	"SpecificationValues": [{
		"NatureOptionID": 3486,
		"OptionValue": "a",
		"NatureID": 345,
		"CommodityID":'null'
	}]
}
#timeout 最大响应时间，超时处理
r3 = requests.post('http://103.6.223.203:8016/Goods/Edit',
                   json=data,headers=hearders,timeout=10)
print(r3.json())
