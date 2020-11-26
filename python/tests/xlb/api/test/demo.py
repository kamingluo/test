from django.views.generic.base import View
from django.http import HttpResponse

class request_demo(View):
    def get(self,request):
        return HttpResponse("这是get请求啦啦啦啦")

    def post(self,request):
        return HttpResponse("这是post请求,发送邮件！")

    def delete(self,request):
        return HttpResponse("这是detele请求")

    def put(self,request):
        return HttpResponse("这是put请求")


#
# if __name__ == '__main__':
#     unittest.main()
