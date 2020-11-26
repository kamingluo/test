from .operate_db import Operatedb
import json
import re

class Process():
    def __init__(self):
        self.db = Operatedb()

    def headerdepend(self,headerdata,step_id,depend_steps,depend_keys):
        # 判断请求body是否需要依赖接口
        if depend_steps != "":
            #根据依赖用例和步骤,获取前置条件的返回健和值
            sql = '''SELECT return_key,return_value FROM case_step WHERE step_id = (
                    SELECT prepose_header_step FROM case_step WHERE step_id = "%s" )''' %(str(step_id))

            sqlresult = self.db.execute(sql)

            return_keys = sqlresult[0][0]
            return_values = sqlresult[0][1]
            headerdata = self.replace(headerdata,return_keys,return_values,depend_keys)
            headerdata = eval(headerdata)
            return headerdata
        else:
            return headerdata


    def datadepend(self,url,bodydata,step_id,depend_steps,depend_keys):
        # 判断请求body是否需要依赖接口
        if depend_steps != "":
            # 根据依赖用例和步骤,获取前置条件的返回健和值
            sql = '''SELECT return_key,return_value FROM case_step WHERE step_id = (
                          SELECT prepose_body_step FROM case_step WHERE step_id = "%s" )''' % (str(step_id))

            sqlresult = self.db.execute(sql)

            return_keys = sqlresult[0][0]
            return_values = sqlresult[0][1]
            if bodydata != "":
                bodydata = self.replace(bodydata, return_keys, return_values, depend_keys)
                # 字符串数据类型转为字典类型
                print("字符串数据类型转为字典类型!!!!!!!!!", bodydata)
                bodydata = eval(bodydata)
                return url, bodydata

            else:
                url = self.replace(url, return_keys, return_values, depend_keys)
                return url, bodydata
        else:
            return url, bodydata

    def urldepend(self,url,step_id,depend_steps,depend_keys):
        pass



    def replace(self,data,return_keys,return_values,depend_keys):
        data = str(data)
        return_keys = return_keys.split(",")
        return_values = return_values.split(",")
        depend_keys = depend_keys.split(",")
        # 遍历需要替换的参数的数量

        for var_num in range(0, len(depend_keys)):
            # 获取替换参数对应返回参数位置的索引号
            res_index = return_keys.index(depend_keys[var_num])
            replace_value = "${" + depend_keys[var_num] + "}"
            # 根据索引号，获取替换字段对应的返回参数
            data = data.replace(replace_value, return_values[res_index])

        # 字符串数据类型转为字典类型
        replace_data = data
        # replace_data = eval(data)
        print("替换后的参数！！！！！！！！！！！！！！！！！！！！！！！！！！！", replace_data)

        return replace_data

    def get_response_data(self,response_data,return_key,step_id):
        res = json.dumps(response_data)
        #res = response_data
        print ("get_response_data----------.",res)
        if return_key != '':
            replace_datas = []

            # 需要储存多个数据时，for循环遍历出数据数量
            return_key = return_key.split(",")
            for keynum in range(0, len(return_key)):
                start_return__key = "\"" + return_key[keynum] + "\": \""
                end_return_key= "\""
                replace_data = re.findall('''%s(.+?)%s''' % (start_return__key, end_return_key), res)

                replace_datas.append(replace_data[0])
            replace_datas = ",".join(replace_datas)

            sql = '''UPDATE case_step SET return_value = "%s" WHERE step_id = "%s" '''%(replace_datas,step_id)
            self.db.execute(sql)

    def initialize_case(self,case_id):
        if case_id == "all":
            initialize_step = "UPDATE case_step SET result = 0"
            initialize_case = "UPDATE test_case SET result = 0"

        else:
            initialize_step = "UPDATE case_step SET result = 0 WHERE case_id = '%s'"%case_id
            initialize_case = "UPDATE test_case SET result = 0 WHERE case_id = '%s'"%case_id
        self.db.execute(initialize_step)
        self.db.execute(initialize_case)



