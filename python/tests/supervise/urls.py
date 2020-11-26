
from django.urls import path,include
from . import  views
from supervise.api.run_api.apitest import test_run_api
from supervise.api.run_api import handleapi
urlpatterns = [
    path('api/runapi/apitest', test_run_api.as_view()),
    path('api/runapi/handleapi/handleall', handleapi.handleall),
    path('api/runapi/handleapi/handle', handleapi.handle),
]
