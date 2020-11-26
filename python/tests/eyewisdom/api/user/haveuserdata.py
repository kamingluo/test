from django.http import HttpResponse
import json
from eyewisdom.common.login import ew_login
from eyewisdom.common.req import req
from eyewisdom.conf import hostdata
import requests

def index(request):
    bodydata = json.loads(request.body)
    result = ew_login(bodydata)#获取登录信息
    dataList=[]
    dataList.append(result)

    cookie=result["data"]["cookie"] #获取到cookie
    service=bodydata["service"]
    if service== 1:
        host = hostdata["test"]
    else:
        host = hostdata["production"]

    url=host +"hospitalUser/currentUserInfo"

    userresult=req(url,cookie=cookie,methods="get",case_name="获取用户信息")
    dataList.append(userresult)
    testdata = {"massage":"请求成功","code":200,"dataList": dataList}
    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")




