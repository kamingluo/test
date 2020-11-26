import sys
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.core import serializers
#引入这个app封装好的方法
from cyl.common.cylapp.login import login

def applogin(request):
    bodydata = json.loads(request.body)
    dataList = login(bodydata)
    # dataList.append(resdata)
    testdata = {"massage":"请求成功","code":200,"dataList": dataList}
    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")




