
from django.urls import path,include
from . import  views
from cyl.api.login import case
from cyl.api.login import test
from cyl.api.login import testemail
from cyl.api.login import testrequst
from cyl.api.login import applogin
urlpatterns = [
    path('', views.index ),
    path('login/case', case.index ),
    path('login/test', test.index ),
    path('login/testemail', testemail.sentemail),
    path('login/testrequst', testrequst.sentrequst),
    path('login/addbaiduad', testrequst.addbaiduad),
    path('login/addappbaiqingten', testrequst.addappbaiqingten),
    path('login/listbyuser', testrequst.listbyuser),
    path('login/addadmin', testrequst.addadmin),
    path('login/applogin', applogin.applogin),
]
