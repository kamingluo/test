from django.shortcuts import render
#coding:utf-8
# Create your views here.
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_http_methods,require_POST
from django.db.utils import *

from .common.operate_db import Operatedb
from .common.send_request import Send
from .common.api_parameter import Process
from .common.util import Util
from .common.assert_manage import Assert
from django.views import View


class test(View):
    def __init__(self):
        pass

    def get(self,request,*arg,**kwargs):
        pass
    def post(self,request,*arg,**kwargs):
        pass



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def casemanager(request):
    db = Operatedb()
    sql = "select * from case_step"

    rows = db.query(sql)
    print (type(rows[0]["expectResult"]))

    testdata = {"code": 200,"massage": "success", "data":{"rows":rows}}

    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")
def caselist(request):
    db = Operatedb()
    # proc = Process()
    # proc.initialize_case()
    # ass = Assert()
    # ass.case_result()


    sql = "SELECT * FROM test_case"
    rows = db.get_db_rows(sql)

    testdata = {"code": 200,"massage": "success", "data":{"rows":rows}}

    return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")




@require_POST
def run(request):
    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)

    db = Operatedb()
    req = Send()
    proc = Process()
    ut = Util()
    ass = Assert()

    #初始化用例和步骤的测试结果
    case_id = bodydata["case_id"]
    proc.initialize_case(case_id)


    runall = "SELECT * FROM test_case ts INNER JOIN case_step cs \
          ON ts.case_id = cs.case_id \
          WHERE ts.is_run = 1 AND cs.is_run = 1"

    runid = "SELECT * FROM case_step WHERE case_id = %s and is_run = 1"%(case_id)
    #判断是批量运行还是单个用例运行
    sql = runall if case_id == "all" else runid

    rows = db.get_db_rows(sql)

    for row in rows:
        # header是否需要依赖前置case
        headerdata = proc.headerdepend(row["header"],
                            row["step_id"],
                            row["prepose_header_step"],
                            row["prepose_header_key"]
                            )


        # 序列化json
        bodydata = json.loads(row["body"]) if row["body"] != "" else row["body"]

        #url,body是否需要依赖前置case
        url,bodydata = proc.datadepend(
                            row["url"],
                            bodydata,
                            row["step_id"],
                            row["prepose_body_step"],
                            row["prepose_body_key"]
                            )


        #检查body是否需要生成测试数据
        bodydata = ut.replace_testdata(bodydata)

        response_data = req.run(
                            method = row["method"],
                            url = url,
                            data = bodydata,
                            headers = headerdata
                                )
        #对象转为字典
        # response_data = response_data.json()

        response_data = ass.level(row["assert_level"],row["step_id"],response_data,row["expect_result"],row["expect_code"])

        #http状态码非200时，跳出本次循环
        if response_data == False:
            continue

        #判断是否需要返回数据
        proc.get_response_data(response_data,
                               row["return_key"],
                               str(row["step_id"])
                               )
    #根据用例的测试步骤,判断最终测试用例结果
    ass.case_result()
    res_message = {"code": 200,"massage": "success"}

    return HttpResponse(json.dumps(res_message, ensure_ascii=False), content_type="application/json,charset=utf-8")


def addcase(request):

    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)

    db = Operatedb()


    add_rowdata = "INSERT `test_case`(case_id,project, title) VALUES ('%s','%s', '%s')"\
                  %(bodydata['case_id'],bodydata['project'],bodydata['title'])

    #新增case_id是否已存在
    caseid_exist = "SELECT * FROM test_case WHERE case_id = %s"% bodydata['case_id']
    exist_row = db.get_db_rows(caseid_exist)
    print("exist_row",exist_row)

    whether_exe = db.execute(add_rowdata) if exist_row == [] else False
    print ("whether_exe",whether_exe)

    success_message = {"code": 200, "massage": "新增成功"}
    notexistid_message = {"code": 200, "massage": "caseid已存在"}

    res_message = success_message if whether_exe != False else notexistid_message

    return HttpResponse(json.dumps(res_message, ensure_ascii=False), content_type="application/json,charset=utf-8")

def updatecase(request):
    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)

    db = Operatedb()
    update_rowdata = "UPDATE test_case SET case_id = '%s',project = '%s',title = '%s',is_run = %s WHERE id = %s"\
                     %(bodydata['case_id'],bodydata['project'],bodydata['title'],bodydata['is_run'],bodydata['id'])

    print(update_rowdata)
    try:
        db.execute(update_rowdata)
        res_message = {"code": 200, "massage": "更新成功"}
    except Exception as ie:
        print (ie)
        res_message = {"code": 200, "massage": "error:"+ str(ie)}
    return HttpResponse(json.dumps(res_message, ensure_ascii=False), content_type="application/json,charset=utf-8")

def delectcase(request):
    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)

    db = Operatedb()
    delect_rowdata = "DELETE FROM `test_case` WHERE `id` = %s" %bodydata['case_id']
    db.execute(delect_rowdata)

    res_message = {"code": 200, "massage": "删除成功"}
    return HttpResponse(json.dumps(res_message, ensure_ascii=False), content_type="application/json,charset=utf-8")

def steplist(request):
    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)

    # case_id = request.GET.get("case_id")

    db = Operatedb()
    sql = "SELECT * FROM case_step WHERE case_id = %s" % bodydata['case_id']
    # sql = "SELECT * FROM case_step WHERE case_id = %s" %bodydata['case_id']

    rows = db.get_db_rows(sql)
    successdata = {"code": 200,"massage": "success", "data":{"rows":rows}}
    nonedata = {"code": 200,"massage": "暂无数据", "data":{"rows":rows}}

    print("sql结果", rows)
    #判断用例的步骤是否为空
    response_data = nonedata if rows == [] else successdata

    return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type="application/json,charset=utf-8")

def addstep(request):
    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)

    db = Operatedb()

    add_rowdata = "INSERT `case_step` (case_id,step_id,is_run,step_title,url,method,prepose_header_step,prepose_header_key,header,prepose_body_step,prepose_body_key,body,return_key,return_value,assert_level,expect_result) " \
                  "VALUES (%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                  %(bodydata['case_id'],bodydata['step_id'],bodydata['is_run'],bodydata['step_title'],
                    bodydata['url'],bodydata['method'],bodydata['prepose_header_step'],bodydata['prepose_header_key'],
                    bodydata['header'],bodydata['prepose_body_step'],bodydata['prepose_body_key'],bodydata['body'],
                    bodydata['return_key'],bodydata['return_value'],bodydata['assert_level'],bodydata['expect_result'])

    print (add_rowdata)

    db.execute(add_rowdata)
    res_message = {"code": 200, "massage": "新增成功"}

    return HttpResponse(json.dumps(res_message, ensure_ascii=False), content_type="application/json,charset=utf-8")

def updatestep(request):
    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)

    db = Operatedb()
    update_rowdata = "UPDATE case_step SET is_run = '%s',step_title = '%s',url = '%s',\
                    method = %s,\
                    prepose_header_step = '%s',\
                    prepose_header_key = '%s',\
                    header = '%s',\
                    prepose_body_step = '%s',\
                    prepose_body_key = '%s',\
                    body = '%s',\
                    return_key= '%s',\
                    return_value = '%s',\
                    assert_level = '%s',\
                    expect_result = '%s' WHERE step_id = '%s'" \
                %(bodydata['is_run'], bodydata['step_title'],
                 bodydata['url'], bodydata['method'], bodydata['prepose_header_step'], bodydata['prepose_header_key'],
                 bodydata['header'], bodydata['prepose_body_step'], bodydata['prepose_body_key'], bodydata['body'],
                 bodydata['return_key'], bodydata['return_value'], bodydata['assert_level'], bodydata['expect_result'],bodydata['step_id'])
    print (update_rowdata)
    exe_result = db.execute(update_rowdata)
    print ("sql执行结果",exe_result)

    res_message = {"code": 200, "massage": "更新成功"}

    return HttpResponse(json.dumps(res_message, ensure_ascii=False), content_type="application/json,charset=utf-8")


def delectstep(request):
    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)

    db = Operatedb()


def updatestep_runstatus(request):
    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)
    db = Operatedb()
    update_isrun = "UPDATE case_step set is_run = %s WHERE id = %s"%(bodydata["is_run"],bodydata["id"])
    exe_result = db.execute(update_isrun)
    print ("sql执行结果",exe_result)

    res_message = {"code": 200, "massage": "更新成功"}
    return HttpResponse(json.dumps(res_message, ensure_ascii=False), content_type="application/json,charset=utf-8")

def updatecase_runstatus(request):
    bodydata = request.body
    bodydataStr = bodydata.decode('utf-8')
    bodydata = json.loads(bodydataStr)
    db = Operatedb()
    update_isrun = "UPDATE test_case set is_run = %s WHERE id = %s"%(bodydata["is_run"],bodydata["id"])
    exe_result = db.execute(update_isrun)
    print ("sql执行结果",exe_result)

    res_message = {"code": 200, "massage": "更新成功"}
    return HttpResponse(json.dumps(res_message, ensure_ascii=False), content_type="application/json,charset=utf-8")
