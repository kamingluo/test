from django.views.generic.base import View
from django.http import HttpResponse
from xlb import models
import json
from django.core import serializers
from django.http import JsonResponse
class request_demo(View):
    def get(self,request):
        lst_my_model = models.Publisher.objects.all()#models查询数据库
        model_data = []
        #循环取出数据并处理
        for item in lst_my_model:
            item.__dict__.pop( "_state" )
            model_data.append( item )
        model_data = serializers.serialize("json", model_data)#将结果转换成JSON格式
        newdata=json.loads(model_data)#将json格式数据转换为字典
        #循环取出操作数据合并
        for newitem in newdata:
            newitem.pop('model')#去除model键值
            fields=newitem["fields"]#拿出fields值
            newitem.update(fields)#拿fields值合并
            newitem.pop('fields')#去除fields值
        return JsonResponse(newdata,safe=False )

        print("下面的是单条信息取出，转成json格式")
        my_model = models.Publisher.objects.get( id=1 )
        # 打印 my_model.__dict__ 发现有一个"_state"，
        # 不是我们Model定义的内容，需要去除
        my_model.__dict__.pop( "_state" ) #需要去除，否则不能 Json化
        return JsonResponse( my_model.__dict__, safe=False )
        return HttpResponse("这是get请求啦啦啦啦")

    def post(self,request):
        lst_my_model = models.Publisher.objects.all().values("id","name","image")
        model_data = []
        #循环取出数据并处理
        for item in lst_my_model:
            model_data.append( item )
        print(type(model_data))
        testdata = {"massage":"这是post请求！","code":200,"dataList": model_data}
        return HttpResponse(json.dumps(testdata, ensure_ascii=False), content_type="application/json,charset=utf-8")

    def delete(self,request):
        return HttpResponse("这是detele请求")

    def put(self,request):
        return HttpResponse("这是put请求")


#
# if __name__ == '__main__':
#     unittest.main()
