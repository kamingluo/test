import sys
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.core import serializers

#引入这个app封装好的方法
from cyl.common.cyladmin.login import login

#引入项目封装好的方法
sys.path.append("../../../")
from common.sqlData import handle

#引入配置文件
from cyl.conf import hostdata

def index(request):
    service=0
    data={"username": "root", "password": "123456789"}
    if service== 1:
        token = login(data,service)
    else:
        token = login(data)
    
    return HttpResponse(json.dumps(token, ensure_ascii=False), content_type="application/json,charset=utf-8")




