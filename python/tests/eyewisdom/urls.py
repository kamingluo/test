from django.urls import path,include
from . import  views
from eyewisdom.api.login import test
from eyewisdom.api.user import haveuserdata
urlpatterns = [
    path('', views.index ),
    path('api/login/test', test.index ),
    path('api/user/haveuserdata', haveuserdata.index ),
]
