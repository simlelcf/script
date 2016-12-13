#_*_ coding:utf-8 _*_
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import  re
import json
hosturl=raw_input("please input login html:")
posturl=hosturl+'/index.php'
cj=cookielib.LWPCookieJar()
cookie_support=urllib2.HTTPCookieProcessor(cj)
opener=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)
h=urllib2.urlopen(hosturl).read()
def doma(html):
  x=re.findall('"\w{32}"',html)
  y=x[0]
  m = re.findall('"([^"]+)"', y)
  m=m[0]
  return  m 
passwd="7903bdff92c8fef9768bc00aeff6a0a505d786cce56898ea4fba21d08def803589d9bc62f116dc544f2fa550a2c1279c2e50bdc01b3d94dca1be9bbbe07c9b0f"
headers ={
        'Accept':'*/*' ,
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':hosturl,
        'Accept-Language':'en-GB,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        'Accept-Encoding':'gzip, deflate, br',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        'Host':'192.168.4.69:2000'
    }
values={"language":"zh-cn","param_username":"admin","param_password":passwd,doma(h):"1","task":"login","command":"login"}
data=urllib.urlencode(values)
request=urllib2.Request(posturl,data,headers)
print "成功登ddos系统"
html1=urllib2.urlopen(request).read()
def  adduser(username,password,):
   add={"command":"add","param_username":"","param_submit_type":""}
   data=urllib.urlencode(add)
   request1=urllib2.Request(hosturl+'/index.php?t=system_user',data)
   html=opener.open(request1).read()
   user_date={"param_username":username,"param_password":password,"param_password_rewrite":password,"param_login_address":"","param_login_mode_web":"on","param_login_mode_cli":"administrator","command":"add","param_submit_type":"submit",doma(html):"1","setp":"2","edit":"%E 6%8F%90E4%%BA%A4"}
   data=urllib.urlencode(user_date)
   request1=urllib2.Request(hosturl+'/index.php?t=system_user',data)
   response=opener.open(request1).read()
   print "this is success  add  username "

