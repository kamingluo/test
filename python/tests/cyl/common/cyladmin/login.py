from django.db import connection
from cyl.conf import hostdata
import requests

def login(data=None,host=None):
    
    if host== None:
        host = hostdata["test"]
    else:
        host = hostdata["production"]
    url= host +'api/appbackend/admin/login'
    response = requests.post(url= url,data=data)
    resdata = response.json()
    token=resdata["data"]
    return token

