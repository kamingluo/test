import requests
import json


class Send():
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    def run(self, method, url, data, headers=''):
        if headers == '':
            headers = self.headers
        else:
            headers = headers

        # 字典格式编码为json格式
        data = json.dumps(data)

        if method == 1:
            print("headers--------------------------->",type(headers),headers)
            print("url,",url)
            response = requests.post(url, data, headers=headers, verify=False)
        elif method == 0:
            print("headers--------------------------->",type(headers),headers)
            print("url,",url)
            response = requests.get(url=url, headers=headers, verify=False)

        response.encoding = 'utf-8'

        return response