from django.db import connection

class Operatedb():
    def __init__(self):
        pass

    def get_db_rows(self,sql):
        cursor = connection.cursor()
        # sql = "select * from polls_question"
        cursor.execute(sql)

        rowdata = cursor.fetchall()
        # 获取数据表的字段名称列表
        col_names = [desc[0] for desc in cursor.description]

        result = []
        #print(rowdata)
        for row in rowdata:
            objDict = {}
            # 通过枚举得到每一行的索引下标和数据
            for index, value in enumerate(row):
                #print("index, value:", index, value)
                # 根据索引下标，填入字段名称和数据
                objDict[col_names[index]] = value
            result.append(objDict)
        return result

    def execute(self,sql):
        cursor = connection.cursor()
        cursor.execute(sql)
        rowdata = cursor.fetchall()
        return rowdata






