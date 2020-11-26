import json
from django.http import HttpResponse

#引入这个app封装好的方法
from xlb.common.pc.login import pc_login

#引入定义数据
from xlb.req_data.work import maintenance

#引入封装好的请求
from xlb.common.pc.req import req

#创建维修工单
def update_maintenance(request):
    dataList = []
    bodydata = json.loads(request.body)

    #获取登录信息
    login_data = pc_login(bodydata)
    dataList.append(login_data)

    token=login_data["data"]["token"]

    data=req(url='wstore/api/analysisLog/create',data=request.body,token=token,service=0)


    testdata = {"massage":"请求成功","code":200,"dataList": dataList}
    # return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return HttpResponse(data, content_type="application/json,charset=utf-8")



