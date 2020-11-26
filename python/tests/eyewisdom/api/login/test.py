from django.http import HttpResponse
import json
from eyewisdom.common.login import ew_login
from xlb import models

def index(request):
    ret = models.Book.objects.all().values('id','title')
    print(type(ret), ret.query)
    for item in ret:
        print("打印拿到的数据")
        print(item, type(item))


    bodydata = json.loads(request.body)
    result = ew_login(bodydata)#获取登录信息
    dataList=[]
    dataList.append(result)
    testdata = {"massage":"请求成功","code":200,"dataList": dataList}
    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")



