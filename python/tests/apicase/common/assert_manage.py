import json_tools
import json
from .operate_db import Operatedb
import re

class Assert():
    def __init__(self):
        self.db = Operatedb()


    def level(self,level,step_id,res_data,expect_result,expect_code):
        self.result_pass = "UPDATE case_step SET result = '%s' WHERE step_id = '%s'" % (1, step_id)
        self.result_fail = "UPDATE case_step SET result = '%s' WHERE step_id = '%s'" % (2, step_id)


        if res_data.status_code == 200:
            #断言返回的code值
            if self.diff_code(res_data,expect_code):
                if  level == 0:
                    self.db.execute(self.result_pass)
                    return res_data.json()
                elif level == 1:
                    self.diff_text(res_data, expect_result)
                    return res_data.json()
                elif level == 2:
                    self.diff_json(res_data, expect_result)
                    return res_data.json()
            else:
                self.db.execute(self.result_fail)
                return False

        else:
            self.db.execute(self.result_fail)
            return False

    def diff_code(self,res_data,expect_code):
        pattern = re.compile(expect_code)
        result = pattern.findall(res_data.text)
        if result == []:
            print(expect_code, "code匹配失败")
            return False
        else:
            print(expect_code, "code匹配成功")
            return True


    def diff_text(self,res_data,expect_result):
        expect_result_list = expect_result.split("|")
        diff_success = []
        diff_fail = []

        for expect_res in expect_result_list:
            pattern = re.compile(expect_res)
            result = pattern.findall(res_data.text)
            print("匹配结果:", result)
            if result == []:
                print(expect_res, "文本匹配失败")
                diff_fail.append(expect_res)
            else:
                print(expect_res, "文本匹配成功")
                diff_success.append(expect_res)

        if diff_fail == []:
            self.db.execute(self.result_pass)
        else:
            self.db.execute(self.result_fail)



    def diff_json(self,res_data,expect_result):
        # 对象转为字典
        #res_data = res_data.json()
        res_data = res_data.text

        if expect_result != "":

            print("预期结果：",type(expect_result),expect_result)
            print("实际结果：",type(res_data),res_data)


            diff_result = json_tools.diff(expect_result,res_data)

            print ("diff_result-------------------->>>",diff_result)

            if diff_result == []:
                print ("pass-----------------------------------------------------------")
                self.db.execute(self.result_pass)
            else:
                print ("fail-----------------------------------------------------------")
                self.db.execute(self.result_fail)


    def case_result(self):
        runcase = "SELECT id FROM test_case WHERE is_run = 1"
        case_rows = self.db.get_db_rows(runcase)
        for case_row in case_rows:
            print ("case_result---------------------------------",type(case_row),case_row)
            step_result = "SELECT result FROM case_step WHERE case_id = '%s'" %(case_row["id"])
            step_rows = self.db.execute(step_result)

            print (step_rows)
            #用例失败
            if  ('2',) in step_rows:
                case_fail = "UPDATE test_case SET result = '%s' WHERE id = '%s'" % (2, case_row["id"])
                self.db.execute(case_fail)
            #用例通过
            elif ('1',) in step_rows:
                case_pass = "UPDATE test_case SET result = '%s' WHERE id = '%s'" % (1, case_row["id"])
                self.db.execute(case_pass)
            #用例不运行
            else:
                case_stop = "UPDATE test_case SET result = '%s' WHERE id = '%s'" % (0, case_row["id"])
                self.db.execute(case_stop)





