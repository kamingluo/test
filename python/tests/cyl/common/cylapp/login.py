from django.db import connection
from cyl.conf import appdata
from cyl.common.apiData import apihandle
import requests

def login(data):
    service=data["service"]
    if service == 1:
        host = appdata["test"]
    else:
        host = appdata["production"]
    mobile=data["mobile"]
    sendSMSurl= host +'api/owner/aiche/appusers/sendSMS'
    sendSMS={
    "imei": "00000000-6d1e-a7ed-0000-00000e39540e",
    "limitCode": "zq9EagC9aFY0CJ0J4jZ4xlp2lgGAeE3g54caf03c1c2571c45bb4e63c1ea9f17a",
    "mobile": mobile
    }
    responseSMS = requests.post(url= sendSMSurl,data=sendSMS)
    SMSresult=apihandle(responseSMS,"发送验证码")
    # responseSMS_time = responseSMS.elapsed.total_seconds()  # 获取实际的响应时间
    # SMSdata = responseSMS.json()
    # SMSresult={"data":SMSdata,"response_time":responseSMS_time,"case_name":"发送验证码","status":0}
    # print (SMSresult)

    loginurl= host +'api/owner/aiche/appusers/login'
    responselogin = requests.post(url= loginurl,data=data)
    loginresult=apihandle(responselogin,"登录")
    # responselogin_time = responselogin.elapsed.total_seconds()  # 获取实际的响应时间
    # logindata = responselogin.json()
    # loginresult={"data":logindata,"response_time":responselogin_time,"case_name":"登录","status":0}
    # print(loginresult)


    return SMSresult,loginresult

