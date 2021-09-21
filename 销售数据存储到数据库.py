import xlrd
import pymysql
wd = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)
con=pymysql.connect(host="localhost",user="root",password="123456",database="excle")
cursor=con.cursor()    #创建控制台
a=0
excel=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
for i in excel:
    sql = "CREATE TABLE if not exists " + i + " (`日期` VARCHAR(10),`服装名称` VARCHAR(10),`价格/件` FLOAT,`本月库存数量` FLOAT,`销售量/每日` FLOAT)"
    print(sql)

    cursor.execute(sql)
    con.commit()
    sheet = wd.sheet_by_index(a)
    rows = sheet.nrows  #读取行数
    cols = sheet.ncols  #读取列数
    for row in range(1, rows):  #循环所有行数
        date = sheet.row_values(row)
        sql1 = "insert into " + i + " values (%s,%s,%s,%s,%s)"
        print(sql1)
        param1 = date
        cursor.execute(sql1, param1)
        con.commit()
    a = a + 1
cursor.close()
con.close()

