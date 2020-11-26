from django.db import connection
from xlb.conf import hostdata
import requests
import json

def req(url=None,service=1,token=None,cookies=None,data=None,methods="post"):
    #测试服还是正式服
    
    if service== 1:
        host = hostdata["pc_test"]
    else:
        host = hostdata["pc_production"]

    #拼接请求地址
    req_url= host + url
    print(req_url)

    if token!=None:
        headers = {'content-type': 'application/json',
           'authorization': token }
    else:
        headers = {'content-type': 'application/json'}

    

    if methods=="post":
        res_data = requests.post(url=req_url, data=data, headers=headers)
    else:
        res_data = requests.get(url=req_url, params=data,headers=headers) 



    
    return res_data

