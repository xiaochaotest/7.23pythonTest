#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Peng Chao



import  requests

'''
cookie的处理步骤：
1、登录发送请求
2、登录成功后
3、获取session信息并且返回
'''
#方式一，通过登陆返回session，获取登陆以后的信息
# def login():
# 	'''登录获取登录后的session信息，在客户端看到的虽然是Cookies，但是实际只是请求头的标识，实际上是session的整个信息，
# 	Cookies存储在客户端，是不安全的'''
# 	r=requests.post('http://117.39.63.66:20080/auth/login',
# 	                data={'username':'system','password':'123456'})
# 	#拿到session
# 	print(r.cookies['session'])
# 	#返回拿到的session
# 	return r.cookies['session']
#
# def getInfo():
# 	r = requests.get('http://117.39.63.66:20080/depot/parks/1/profile',
# 	                 #取登陆成功后返回的session
# 	                 cookies={'session':login()})
# 	print(r.text)
# getInfo()
# #方式二，通过请求头的方式获取登陆以后的信息（这样的方式不好，因为Cookie都会有过期时间的）
# def getInfo2():
# 	r=requests.get('http://117.39.63.66:20080/depot/parks/1/profile',
# 	               headers={'Cookie':'_gitlab_session=0158fe10ca80a71a434589e50ffd135a; remember_user_token=BAhbB1sGaTBJIiIkMmEkMTAkbVFKajRwMFJmL3pRdlh0SmoxS1Z6LgY6BkVU--e50b97c22bebdb6859c0a0bd6e64075fc8e2557f; port=20080; session=.eJwdjrFqwzAURX-lvDlDokaLIUtRImp4Eg62hd4SaOxWfpYWpxmskH-P2uFyh8Ph3gdcvpfxFqD6Xe7jBi7TANUD3r6gAuIfaV0jDTerUTGgOAfSFGx73fr8EY3CPak6GldPvu0D8vHd8zkRD0zJS2qHiXTh2gsjup1nv0UVitesf20VipJ94dLqmq3rA7ljJv0pSZ0Sch19jsk4lKi7ldxp9nmYMJkZRT9T2TWZErXdAZ4buN_G5f8_7OD5AiTCRx4.Disn-A.ZA9ZnACp68SM-ZVYmkuX8_9nUns'})
# 	print(r.text)
# #这样写每请求一次，就会登陆一次，
# def getData():
# 	r=requests.get('http://117.39.63.66:20080/settings/option/other/data',
# 	               cookies={'session':login()})
# 	print(r.text)
#
# getInfo2()
# getData()
#
# def login():
# 	'''登录获取登录后的session信息
# 	把session信息写到文件中
# 	'''
# 	r=requests.post('http://117.39.63.66:20080/auth/login',
# 	                data={'username':'system','password':'123456'})
# 	#把登陆的信息写入到文件中
# 	with open('cookie','w') as f:
# 		f.write(r.cookies['session'])
# #读取写入文件中的信息
# def getSession():
# 	with open('cookie','r') as f:
# 		return f.read()
#
# def getInfo():
# 	r = requests.get('http://117.39.63.66:20080/depot/parks/1/profile',
# 	                 cookies={'session':getSession()})
# 	print(r.text)
#
# def getData():
# 	r=requests.get('http://117.39.63.66:20080/settings/option/other/data',
# 	               cookies={'session':getSession()})
# 	print(r.text)
#
# print(getSession())

import  unittest

class Cookie(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		r=requests.post('http://117.39.63.66:20080/auth/login',
			                data={'username':'system','password':'123456'})
		with open('cookie','w') as f:
			f.write(r.cookies['session'])

	@classmethod
	def tearDownClass(cls):
		pass

	def getSession(self):
	#	获取session信息
		with open('cookie','r') as f:
			return f.read()

	def test_getinfo(self):
		r = requests.get('http://117.39.63.66:20080/depot/parks/1/profile',
			                 cookies={'session':self.getSession()})
		print(r.text)

	def test_getData(self):
		r=requests.get('http://117.39.63.66:20080/settings/option/other/data',
			               cookies={'session':self.getSession()})
		print(r.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)


'''Cookie的获取以及实战'''
#
# data={'email':'970138074@qq.com','icode':'','origURL':'http://www.renren.com/home',
#       'domain':'renren.com','key_id':'1','captcha_type':'web_login',
#       'password':'658ad9d22407ed607048fc41f388cec8798a77e61a29935b24ba909a1aa89923',
#       'rkey':'9e75e8dc3457b14c55a74627fa64fb43','f':'http%3A%2F%2Freg.renren.com%2Fxn6218.do%3Fss%3D10756%26rt%3D27'}
#
# def renLogin():
# 	r=requests.post(url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018661516954',
# 	                data=data)
# 	return r.cookies
#
# def info():
# 	'''查看信息'''
# 	data={'month':'7','requestToken':'-505719466','_rtk':'ad9c53b0'}
# 	r=requests.post('http://sc.renren.com/scores/loadBornInfo',
# 	                data=data,
# 	                cookies=renLogin())
# 	print(r.text)
#
# info()
