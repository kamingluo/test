from django.db import connection
# from eyewisdom.conf import hostdata
import requests
import json

def req(url=None,service=1,cookie=None,cookies=None,data=None,methods="post",case_name="测试用例标题"):
    #测试服还是正式服拼接请求地址
    # if service== 1:
    #     host = hostdata["test"]
    # else:
    #     host = hostdata["production"]
    # #拼接请求地址
    # req_url= host + url
    req_url=url#先改成直接传请求接口
    print(req_url)
    if cookie!=None:
        headers = {'content-type': 'application/json',
           'cookie': cookie }
    else:
        headers = {'content-type': 'application/json'}

    if methods=="post":
        res_data = requests.post(url=req_url, data=data, headers=headers)
    else:
        res_data = requests.get(url=req_url, params=data,headers=headers) 

    resdata = res_data.text #拿到返回值
    print("请求接口拿到返回值")
    print(resdata)
    status_code=res_data.status_code#网络请求状态码
    newresdata=None
    status=0
    if status_code==200:
        try:
            print("转换返回值格式")
            newresdata=json.loads(resdata)#将返回值转成json格式，如果不能正常转换，就是返回值错误
        except:
            print("这是错误信息啊")
            status=1
        else:
            print("正常返回")
            status=0
    else:
        status=1
    response_time = res_data.elapsed.total_seconds()  # 获取实际的响应时间
    result={"data":newresdata,"response_time":response_time,"case_name":case_name,"status":status}
    return result

