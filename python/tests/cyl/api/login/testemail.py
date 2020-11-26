import sys
sys.path.append("../../../")
from django.http import HttpResponse
from common.sentEmail import sent
import json


def sentemail(request):
    # return  HttpResponse("这是车有料项目登录模块case！")
    data=sent(title='发送邮件的标题',text='发送邮件的正文',touser=['954087620@qq.com','1020462481@qq.com'],reports="reports/first.html")

    testdata = {"massage": "发送邮件!", "code": 200, "data": data}

    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")



