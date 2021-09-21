import xlwt
import pymysql

xlsx = xlwt.Workbook(encoding="utf-8")
# 1.获取数据库连接
conn = pymysql.connect(host='localhost', database='company', user='root', passwd='123456')
#2.创建控制台
cursor = conn.cursor()

# t_dept表
sql = '''select * from t_dept'''
cursor.execute(sql)
dept = cursor.fetchall()
sheet_dept = xlsx.add_sheet("t_dept", True)
# 创建表头
head_dept = ['deptno', 'dname', 'loc']
for h in head_dept:
    sheet_dept.write(0, head_dept.index(h), h)
# 内容
for d in dept:
    for i in d:
        sheet_dept.write(dept.index(d)+1, d.index(i), i)

# t_employees表
sql = '''select * from t_employees'''
cursor.execute(sql)
employees = cursor.fetchall()
sheet_employees = xlsx.add_sheet("t_employees", True)
# 表头
head_employees = ['empno', 'ename', 'job', 'MGR', 'hiredate', 'sal', 'comm', 'deptno']
for h in head_employees:
    sheet_employees.write(0, head_employees.index(h), h)
# 内容
for e in employees:
    for j in e:
        sheet_employees.write(employees.index(e)+1, e.index(j), j)

xlsx.save("三国集团数据.xls")