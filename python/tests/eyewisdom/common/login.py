from django.db import connection
from eyewisdom.conf import authdata
import requests
import os, sys

def ew_login(data):
    service=data["service"]
    print(service)
    if service== 1:
        host = authdata["test"]
    else:
        host = authdata["production"]
    url= host + 'username=' + data["username"] + '&password=' + data["password"]
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    s=requests.Session()
    response=s.post(url,headers=headers)
    # status_code=response.status_code#状态码!
    # print("打印状态码")
    # print(status_code)
    response_time =response.elapsed.total_seconds()
    # print("打印响应时间")
    # print(response_time)
    # resdata = response.text
    # print("打印返回信息")
    # print(resdata)
    cookie = requests.utils.dict_from_cookiejar(s.cookies)
    # print("打印cookie")
    # print(cookie)
    if cookie != {}:
        print("登录成功，拿到cookie")
        newcookie="vistel_token="+cookie["vistel_token"]
        data={"cookie":newcookie}
        result={"data":data,"response_time":response_time,"case_name":"EW登录拿cookie","status":0}
    else:
        print("登录不成功")
        result={"data":"登录错误，请检查账号或者环境","response_time":response_time,"case_name":"EW登录拿cookie","status":1}
    return result

