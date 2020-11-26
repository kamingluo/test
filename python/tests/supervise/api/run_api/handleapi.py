from django.http import HttpResponse
from common.sqlData import handle
import json
import requests
from django.db import connection
import pymysql as db


def handleall(request):
    service = request.GET.get('service')
    sql = '''UPDATE test_run_api SET service={} '''.format
    sql1 = sql(service)
    cursor = connection.cursor()
    cursor.execute(sql1)
    connection.commit()
    testdata = {"massage": "更新全部完成", "code": 200}
    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")


def handle(request):
    service = request.GET.get('service')
    id = request.GET.get('id')
    sql = '''UPDATE test_run_api SET service={} WHERE id ={}'''.format
    sql1 = sql(service,id)
    cursor = connection.cursor()
    cursor.execute(sql1)
    connection.commit()
    testdata = {"massage": "更新单条完成", "code": 200}
    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")