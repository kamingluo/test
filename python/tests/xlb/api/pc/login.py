import json
from django.http import HttpResponse

#引入这个app封装好的方法
from xlb.common.pc.login import pc_login

#引入定义数据
from xlb.req_data.work import maintenance


def login(request):
    dataList = []

    # #改变数据的值
    # testdata = maintenance
    # maintenance["billUser"]={"kaming":"111"}
    # print(maintenance)
    #拿到post请求需要的数据,并转换为json格式
    bodydata = json.loads(request.body)
    result = pc_login(bodydata)#获取登录信息
    dataList.append(result)
    testdata = {"massage":"请求成功","code":200,"dataList": dataList}
    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")



