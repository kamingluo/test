
def apihandle(response,name):

    response=response
    response_time = response.elapsed.total_seconds()  # 获取实际的响应时间
    data = response.json()
    if data["code"] == 200 or data["code"] == 0 :
        result={"data":data,"response_time":response_time,"case_name":name,"status":0}
    else:
        result={"data":data,"response_time":response_time,"case_name":name,"status":1}
    return result
