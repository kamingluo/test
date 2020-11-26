import pytest
from django.http import HttpResponse


def test_answer(request):
    # return  HttpResponse("这是车有料项目登录模块case！")
    # print ("执行了断言")
    # assert 3 == 1 + 1,print ("错了")
    # print ("执行完了断言")
    #
    # return HttpResponse("kaming", content_type="application/json,charset=utf-8")


    try:
        username = "admin"
        # 输入的用户名不是admin就抛出异常Exception
        if username != "admin":
            raise Exception(f"maybe your privilege is not enough")
        # 可以看到打印的是我们自定义的异常语句
        print ("打印一下")
    except Exception as e:
        return HttpResponse("kaming111", content_type="application/json,charset=utf-8")


    return HttpResponse("kaming222", content_type="application/json,charset=utf-8")


if __name__ =="__main__":
    test_answer()