from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return  HttpResponse("这是修连邦项目xlb!")
