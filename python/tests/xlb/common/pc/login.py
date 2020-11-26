from django.db import connection
from xlb.conf import hostdata
import requests
import os, sys

def pc_login(data):
    service=data["service"]
    if service== 1:
        host = hostdata["pc_test"]
    else:
        host = hostdata["pc_production"]
    url= host +'wstore/api/user/login'
    response = requests.post(url= url,data=data,)
    resdata = response.json()
    response_time = response.elapsed.total_seconds()  # 获取实际的响应时间
    if resdata["code"] == "0":
        #data=resdata["data"]
        data={"token":resdata["data"]["token"],"userId":resdata["data"]["user"]["userId"],"username":resdata["data"]["user"]["username"]}
        result={"data":data,"response_time":response_time,"case_name":"修连邦登录拿token","status":0}
    else:
        result={"data":resdata["msg"],"response_time":response_time,"case_name":"修连邦登录拿token","status":1}
    return result

