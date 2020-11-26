from django.views.generic.base import View
from django.http import HttpResponse
from common.sqlData import handle
import json
import requests
from django.db import connection
import pymysql as db

class test_run_api(View):

    def get(self,request):
        pages = request.GET.get('pages')
        newpages=(int(pages)-1) * 10
        print(newpages)
        #拿到数据表的条数
        counts = "select count(*) as data from {}".format('test_run_api')
        countnum = handle(counts)
        count=countnum[0]['data']


        sql = "SELECT * FROM `test_run_api` order by id desc limit {},10 ".format(newpages)
        resdata = handle(sql)
        # return HttpResponse(json.dumps(resdata, ensure_ascii=False),
        #                     content_type="application/json,charset=utf-8")
        testdata = {"massage": "获取数据成功", "code": 200,"count":count, "data": resdata}

        return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")

    def post(self,request):
        # 拿到post请求需要的数据,并转换为json格式
        bodydata = json.loads(request.body)
        #拿到需要的字符串
        project = "'" +bodydata['project'] + "'"
        name = "'" + bodydata['name'] + "'"
        remarks ="'" + bodydata['remarks'] + "'"
        request_url = "'" + bodydata['request_url'] + "'"
        service = bodydata['service']
        print(service)
        #因为是json数据，所以要转一下
        body1 = bodydata['body']
        body = "'" +  json.dumps(body1)+ "'"
        #利用.format去拼接字符串
        sql = '''INSERT INTO `test_run_api` ( project, name, remarks, body, request_url,service ) VALUES ({},{},{},{},{},{})'''.format
        sql1 = sql(project,name,remarks,body,request_url,service)
        #连接数据库插入
        cursor = connection.cursor()
        cursor.execute(sql1)
        connection.commit()

        testdata = {"massage": "添加数据成功", "code": 200}
        return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")


    def delete(self,request):

        id = request.GET.get('id')
        print (id)
        sql = '''DELETE FROM test_run_api WHERE id = {}'''.format
        sql1 = sql(id)
        cursor = connection.cursor()
        cursor.execute(sql1)
        connection.commit()
        testdata = {"massage": "删除成功", "code": 200}
        return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")


    def put(self,request):
        # 拿到post请求需要的数据,并转换为json格式
        bodydata = json.loads(request.body)
        # 拿到需要的字符串
        id = bodydata['id']
        project = "'" + bodydata['project'] + "'"
        name = "'" + bodydata['name'] + "'"
        remarks = "'" + bodydata['remarks'] + "'"
        request_url = "'" + bodydata['request_url'] + "'"
        service = bodydata['service']
        # 因为是json数据，所以要转一下
        body1 = bodydata['body']
        body = "'" + json.dumps(body1) + "'"
        # 利用.format去拼接字符串
        sql = '''UPDATE test_run_api SET project={},name={},remarks={},body={},request_url={},service={} WHERE id ={}'''.format
        sql1 = sql(project, name, remarks, body, request_url,service,id)
        # 连接数据库插入
        cursor = connection.cursor()
        cursor.execute(sql1)
        connection.commit()

        testdata = {"massage": "更新成功", "code": 200}
        return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")
