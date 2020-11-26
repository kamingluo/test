#coding:utf-8
import datetime
import random
import json


class Util():
    def __init__(self):
        pass

    # 请求参数需要模拟实际数据时，可在json文件里配置表达式，满足条件时替换成测试数据
    def replace_testdata(self, data):
        if data != "":
            data = str(data)
            if "#{statementNo}" in data:
                data = data.replace("#{statementNo}", self.create_statementNo())

            if "#{now_time}" in data:
                data = data.replace("#{now_time}", self.now_time())

            replace_data = eval(data)
            print("errordata------------------------------------------------------------->", data)
            return replace_data
        return data

    #生成修连邦工单号
    def create_statementNo(self):
        now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        firstnum = random.randint(10, 99)
        endnum = random.randint(1000, 9999)

        statementNo = str(firstnum) + now_time + str(endnum)
        return statementNo
    #生成当前时间
    def now_time(self):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now_time
