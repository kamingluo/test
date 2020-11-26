from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('casemanager', views.casemanager, name='casemanager'),
    path('run', views.run, name='run'),
    path('caselist',views.caselist, name='caselist'),
    path('caselist/add',views.addcase, name = 'addcase'),
    path('caselist/update',views.updatecase,name = "updatecase"),
    path('caselist/delectcase',views.delectcase,name = "delectcase"),
    path('steplist', views.steplist, name="steplist"),
    path('steplist/add', views.addstep, name="addstep"),
    path('steplist/update', views.updatestep, name="updatestep"),
    path('steplist/updaterun', views.updatestep_runstatus, name="updatesteprun"),
    path('caselist/updaterun', views.updatecase_runstatus, name="updatecaserun")

]