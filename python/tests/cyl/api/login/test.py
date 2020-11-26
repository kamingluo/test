from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

import json

def index(request):
    # return  HttpResponse("这是车有料项目登录模块test！")
    cursor = connection.cursor()  # 获得一个游标(cursor)对象
    cursor.execute("select * from test")
    rawData = cursor.fetchall()

    col_names = [desc[0] for desc in cursor.description]
    result = []
    for row in rawData:
        objDict = {}
        # 把每一行的数据遍历出来放到Dict中
        for index, value in enumerate(row):
            objDict[col_names[index]] = value
        result.append(objDict)

    testdata = {"massage":"请求消息!!","code":200,"data": result}

    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")



