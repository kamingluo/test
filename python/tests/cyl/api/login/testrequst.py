
from django.http import HttpResponse
from django.db import connection
from django.core import serializers
import json
import requests
import sys
import random
import time




#添加小程序管理人员
def addadmin(request):
    bodydata = json.loads(request.body)
    Cookie=bodydata["Cookie"]
    Authorization=bodydata["Authorization"]
    appid=bodydata["appid"]
    Referer='https://smartprogram.baidu.com/developer/home/member.html?appId={}'.format(appid)
    header={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Cookie": Cookie,
        "Content-Length": '145',
        "Content-Type": "application/json;charset=UTF-8",
        "Referer":Referer,
        "Authorization":Authorization,
        "Origin": "https://smartprogram.baidu.com",
        "Sec-Fetch-Mode": "cors",
        "Connection": "keep-alive",
        "Host": "smartprogram.baidu.com"
    }

    userdata={
        "appId": appid,
        "member": {
            "permissions": "1,2,3,5,6,8,9,62",
            "ukey": "EiWA3L99o2tCtBZdQCku1HH5vHWpeDUO0yhprG4QGI8=",
            "remark": "罗家大明001"
        }
    }

    resdata=json.dumps(userdata)
    url="https://smartprogram.baidu.com/biz/member/add"
    response=requests.post(url,headers=header,data=resdata, verify=False)
    testdata = {"massage": "添加人员成功","code":200}
    return HttpResponse(json.dumps(testdata,ensure_ascii=False),content_type="application/json,charset=utf-8")






#查看百度账号下的小程序账号信息
def listbyuser(request):
    bodydata = json.loads(request.body)
    Cookie=bodydata["Cookie"]
    Stoken=bodydata["Stoken"]
    header={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": Cookie,
        "Host": "smartprogram.baidu.com",
        "Referer": "https://smartprogram.baidu.com/developer/applist.html",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Stoken": Stoken,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
    url="https://smartprogram.baidu.com/biz/app/listByUser"
    response=requests.get(url,headers=header)
    text=response.json()
    num=text["data"]["appList"]
    datalist=[]
    for fruit in num:        
        data={"appname":fruit["appName"],"appid":"{}".format(fruit["appId"]),"adappid":"","feed":[],"banner":[]}
        datalist.append(data)

    testdata = {"massage": "查看百度账号下的小程序账号信息","data":datalist}
    return HttpResponse(json.dumps(datalist,ensure_ascii=False),content_type="application/json,charset=utf-8")






#添加小程序到百青藤
def addappbaiqingten(request):
    bodydata = json.loads(request.body)
    Cookie=bodydata["Cookie"]
    TOKEN=bodydata["X-CSRF-TOKEN"]
    applistheader={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": Cookie,
        "Host": "mssp.baidu.com",
        "Referer": "https://mssp.baidu.com/bqt/appco.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "X-CSRF-TOKEN": TOKEN,
        "X-Request-By": "ERApplication",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    applisturl="https://mssp.baidu.com/v2/client/app/wisedom-app-user/apps"

    #获取小程序列表
    applistresponse=requests.get(applisturl,headers=applistheader,timeout=5)
    text=applistresponse.json()
    applistdata=text["data"]["trades"]

    addheader={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": '437',
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": Cookie,
        "Host": "mssp.baidu.com",
        "Origin": "https://mssp.baidu.com",
        "Referer": "https://mssp.baidu.com/bqt/appco.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "X-CSRF-TOKEN": TOKEN,
        "X-Request-By": "ERApplication",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors"
    }

    addurl="https://mssp.baidu.com/v2/client/app/app-new"
    appdata={
        "appType": 1,
        "code": "",
        "appName": "应用名称",
        "packageName": "应用id",
        "tradeInfo": {
            "text": "购物>购物商城",
            "id": 2669,
            "rootId": 2447,
            "errorId": 0
        },
        "keyword": "购物",
        "description": "轻松买好物，商品价实惠，品种更齐全，多种福利齐发送，补贴买无忧，你的一站式购物平台。",
        "tradeRootId": 2669,
        "tradeSubId": 2669,
        "system": 1,
        "device": 0,
        "appUrl": "",
        "name": "应用名称"
    }

    for fruit in applistdata:
        appdata["appName"]=fruit["appName"]
        appdata["name"]=fruit["appName"]
        appdata["packageName"]=fruit["appId"]
        addresdata=json.dumps(appdata)
        addresponse=requests.post(addurl,headers=addheader,data=addresdata)
        text2=addresponse.json()
        print(text2)


    testdata = {"massage": "添加小程序到百青藤完成啦", "code": 200}
    return HttpResponse(json.dumps(testdata,ensure_ascii=False),content_type="application/json,charset=utf-8")






#查看百度百青腾下面的程序广告id
def sentrequst(request):
    bodydata = json.loads(request.body)
    Cookie=bodydata["Cookie"]
    TOKEN=bodydata["X-CSRF-TOKEN"]
    header={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": Cookie,
        "Host": "mssp.baidu.com",
        "Referer": "https://mssp.baidu.com/bqt/appco.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "X-CSRF-TOKEN": TOKEN,
        "X-Request-By": "ERApplication"
    }
    url="https://mssp.baidu.com/v2/client/app/app-new/list-all"
    response=requests.get(url,headers=header,timeout=5)
    time1 = response.elapsed.total_seconds()  # 获取实际的响应时间
    text = response.json()
    testdata = {"massage": "查看该账号下的广告程序id!!", "code": 200,"time": time1, "data":[text]}
    return HttpResponse(json.dumps(testdata,ensure_ascii=False),content_type="application/json,charset=utf-8")


#添加广告拿到id
def addbaiduad(request):
    print("---------------------")
    print("开始执行添加广告")
    print("---------------------")
    #请求接口
    url="https://mssp.baidu.com/v2/client/appadpos/app-adpos"

    bodydata = json.loads(request.body)
    Cookie=bodydata["Cookie"]
    TOKEN=bodydata["X-CSRF-TOKEN"]
    appSid=bodydata["appSid"]

    header={
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": '430',
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": Cookie,
        "Host": "mssp.baidu.com",
        "Origin": "https://mssp.baidu.com",
        "Referer": "https://mssp.baidu.com/bqt/appco.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "X-CSRF-TOKEN": TOKEN,
        "X-Request-By": "ERApplication"
    }

    bannerdata={
        "name": "banner广告",
        "adpTags": [],
        "basic": {
            "appSid": appSid,
            "appType": 1
        },
        "extra": {
            "appAdpType": 32,
            "fillStyleType": 0,
            "allianceAdps": [],
            "protectRuleId": ""
        },
        "container": {
            "width": 3,
            "height": 1,
            "sizeType": 2
        },
        "fillStyle": {
            "nativead": {},
            "elements": [0, 1, 4]
        }
    }

    feeddata={
            "name": "信息流广告",
            "adpTags": [],
            "basic": {
            "appSid": appSid,
            "appType": 1
            },
            "extra": {
            "appAdpType": 36,
            "fillStyleType": 0,
            "allianceAdps": [],
            "protectRuleId": ""
            },
            "container": {
            "width": 0,
            "height": 0,
            "sizeType": 1
            },
            "fillStyle": {
            "styleTemplateId": [43, 44, 45, 46, 48],
            "nativead": {
                "requiredFields": [7],
                "screenShot": {
                    "width": 1140,
                    "height": 640
                },
                "imageNum": [1]
            },
            "txt": {
                "logoIcon": {
                    "padding": {}
                },
                "image": {
                    "padding": {}
                }
            },
            "adNum": 3,
            "padding": {}
            }
    }

    count = 1
    feedlist = []
    bannerlist = []
    while (count < 15):
        if count < 8:
            str_word = 'newfeed{}'.format(count)
            feeddata["name"]=str_word
            resdata=json.dumps(feeddata)
            response=requests.post(url,headers=header,data=resdata)
            reqdata = response.json()
            adid=reqdata["data"]["id"]
            print(adid)
            feedlist.append(adid)
            time.sleep(2)
            count = count + 1
        else:
            str_word = 'newbanner{}'.format(count)
            bannerdata["name"]=str_word
            resdata=json.dumps(bannerdata)
            response=requests.post(url,headers=header,data=resdata)
            reqdata = response.json()
            adid=reqdata["data"]["id"]
            print(adid)
            bannerlist.append(adid)
            time.sleep(2)
            count = count + 1
    # eval(test)

    newfeedlist=str(feedlist)
    newbannerlist=str(bannerlist)
    testdata = {"massage": "添加广告成功", "code": 200,"feedlist": newfeedlist,"bannerlist": newbannerlist}
    return HttpResponse(json.dumps(testdata,ensure_ascii=False),content_type="application/json,charset=utf-8")


