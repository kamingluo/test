from django.db import connection

def handle(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rowdata = cursor.fetchall()
    # 获取数据表的字段名称列表lalalala
    col_names = [desc[0] for desc in cursor.description]
    result = []
    for row in rowdata:
        objDict = {}
        # 把每一行的数据遍历出来放到Dict中
        for index, value in enumerate(row):
            objDict[col_names[index]] = value
        result.append(objDict)
    return result
