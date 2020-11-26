
from django.urls import path,include
from . import  views
from xlb.api.test.demo import request_demo
from xlb.api.web.login import login_case
from xlb.api.test import pytest_demo
from xlb.api.pc import login
from xlb.api.pc import works
urlpatterns = [
    path('', views.index ),
    path('api/test/demo', request_demo.as_view()),
    path('api/test/pytest', pytest_demo.test_answer),
    path('api/web/login', login_case.as_view()),
    path('api/pc/login', login.login),
    path('api/pc/works/maintenance/update', works.update_maintenance),
]
