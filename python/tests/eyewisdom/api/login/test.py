from django.http import HttpResponse
import json
from eyewisdom.common.login import ew_login

def index(request):
    bodydata = json.loads(request.body)
    result = ew_login(bodydata)#获取登录信息
    dataList=[]
    dataList.append(result)
    testdata = {"massage":"请求成功","code":200,"dataList": dataList}
    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")



