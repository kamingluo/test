from django.views.generic.base import View
from django.http import HttpResponse
from common.sqlData import handle
import json
import requests

class login_case(View):

    def get(self,request):
        sql = 'SELECT * FROM `test_run_api`'
        resdata = handle(sql)
        return HttpResponse(json.dumps(resdata, ensure_ascii=False),
                            content_type="application/json,charset=utf-8")


        text = json.dumps(resdata, ensure_ascii=False)
        # return HttpResponse(text, content_type="application/json,charset=utf-8")

        # text1 = text.json()
        testdata = {"massage": "runapi返回", "code": 200, "data": [text]}

        return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")



        #下面是测试内容，不必管
        # return HttpResponse("这是web模块post请求")
        # sql='''SELECT * FROM `test_run_api` WHERE JSON_CONTAINS(body, '["Mysql"]')'''
        sql = 'SELECT * FROM `test_run_api` where id =1'
        resdata = handle(sql)
        print(resdata[0]['body'])

        testdata=json.loads(resdata[0]['body'])
        print("111111111")
        testdata1=testdata[0]

        return HttpResponse(json.dumps(testdata1['id'], ensure_ascii=False),content_type="application/json,charset=utf-8")
        return HttpResponse(json.dumps(resdata[0]['body']['id'], ensure_ascii=False), content_type="application/json,charset=utf-8")

        text = resdata.json()
        name=text[0].name
        # reqdata = {"massage": "请求接口返回maliang!!", "code": 200, "time": time, "data": [text]}
        reqdata = {"massage": "请求接口返回maliang!!", "code": 200, "time": time, "data": name}

        return HttpResponse(reqdata, content_type="application/json,charset=utf-8")


    def post(self,request):
        bodydata = json.loads(request.body)

        #拿到post请求需要的数据,并转换为json格式
        mobile=bodydata['mobile']
        password = bodydata['password']
        reqdata = {"mobile":mobile, "password": password}
        reqjson=json.dumps(reqdata, ensure_ascii=False)



        response=requests.post('https://apixlbtest.xlbzone.com/wstore/api/user/login', data=reqjson, json=None)
        time = response.elapsed.total_seconds()  # 获取实际的响应时间
        resdata = {"massage": "请求接口返回时间", "code": 200, "time": time}




        return HttpResponse(json.dumps(resdata, ensure_ascii=False),content_type="application/json,charset=utf-8")

