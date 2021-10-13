'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''
import xlrd
import pymysql
class InitPage:
    # wd = xlrd.open_workbook(filename="HKR.xlsx",encoding_override=True)
    #
    # data = []
    # sheet = wd.sheet_by_index(0)
    # rows = sheet.nrows
    # for i in range(1,rows):
    #     rows_values = sheet.row_values(i)
    #     data.append({"username":rows_values[0],"password":str(int(rows_values[1])),"expect":rows_values[2]})
    # print(data)
    #
    # data1 = []
    # sheet = wd.sheet_by_index(1)
    # rows = sheet.nrows
    # for i in range(1,rows):
    #     rows_values = sheet.row_values(i)
    #     data1.append({"username":rows_values[0],"password":str(int(rows_values[1])),"expect":rows_values[2]})
    # print(data1)


    conn = pymysql.connect(host="localhost", user='root', password='root', database='hkrtest')
    cursor = conn.cursor()
    sql = "select * from login "
    cursor.execute(sql)
    x = cursor.fetchall()
    data = []
    for i in range(len(x)):
        data.append({"username": x[i][0], "password": x[i][1], "expect": x[i][2]})

    sql = "select * from error "
    cursor.execute(sql)
    x = cursor.fetchall()
    data1 = []
    for i in range(len(x)):
        data1.append({"username": x[i][0], "password": x[i][1], "expect": x[i][2]})













