import random
import pymysql
#准备四大参数
host="localhost"
user="root"
password="123456"
database="lt"
#只针对增删改
def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    #由链接来创建控制台
    cursor = con.cursor()
    #直接执行sql语句
    cursor.execute(sql,param)
    #提交数据
    con.commit()
    #关闭资源
    cursor.close()
    con.close()
#只针对查询  sql,参数,想要的模式，
def select_date(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany()
    #提交数据
    con.commit()
    #关闭资源
    cursor.close()
    con.close()

menu = '''
        ****************************************
        *     中国工商银行                       *"
        *     账户管理系统                       *"
        *        V1.0                          *"
        "***************************************"
        "                                       "
        *1.开户                                 *"
        *2.存钱                                 *"
        *3.取钱                                 *"
        *4.转账                                 *"
        *5.查询                                 *"
        *6.Bye!                                *"
        ****************************************"
'''
info = '''
                    ------------个人信息------------
                    账号:%s
                    用户名：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s                      
                    开户行名称：%s
                '''
#开户逻辑
def bank_adduser(account,username,password,country,province,street,door,money):
    #查询所有的数据
    sql = "select * from bank"
    date = select_date(sql, [])
    if len(date) >= 100:
        print('用户库已满')
        return 3
    elif account in date:
        return 2
    else:
        sql = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [account,username,password,country,province,street,door,money]
        update(sql, param)
        return 1

# 存钱逻辑
def bank_savemoney(account, money):
    sql = "select * from bank where account=%s"
    param = [account]
    date = select_date(sql,param)
    if  len(date) > 0:
        sql = "update bank set money = money + %s where account = %s"
        param = [money,account]
        update(sql,param)
        a = "select money from bank where account = %s"
        b = select_date(a,account)
        print("卡内余额：",b[0][0])
        return True
    else:
        print("账号不存在")
        return False


# 取钱逻辑
def bank_drawmoney(account, password, money):
    sql = "select * from bank where account=%s "
    param = [account]
    date = select_date(sql, param)
    if len(date) > 0:
        if password == date[0][2]:
            if money < date[0][7]:
                sql = "update bank set money = money- %s where account= %s"
                param = [money, account]
                update(sql, param)
                a = "select money from bank where account = %s"
                b = select_date(a, account)
                print("成功取出金额：", money)
                print("账户余额：", b[0][0])
            else:
                print(3)
                print("当前余额不足！")
        else:
            print(2)
            print("账户密码错误")
    else:
        print(1)
        print("账号不存在！")


# 转账逻辑
def bank_transfer(account1, account2, password, money):
    sql =  "select * from bank where account=%s"
    param = [account1]
    date1 =select_date(sql,param)
    sql = "select * from bank where account=%s"
    param = [account2]
    date2 = select_date(sql, param)
    if len(date1) > 0 :
        if password == date1[0][2]:
            if  len(date2) > 0:
                if money < date1[0][7]:
                    sql1="update bank set money = money - %s where account=%s"
                    param1=[money,account1]
                    update(sql1,param1)
                    sql2= "update bank set money = money + %s where account=%s"
                    param2 = [money, account2]
                    update(sql2, param2)
                    print("转账成功")
                    a = "select money from bank where account= %s"
                    b = select_date(a, account1)
                    print("转出账户余额为：", b[0][0])
                    c = "select money from bank where account= %s"
                    d = select_date(c, account2)
                    print("转入账户余额为：",d[0][0])
                else:
                    print(3)
                    print("余额不足")
            else:
                print(1)
                print("账户不存在！")
        else:
            print(2)
            print("账号密码输入错误！")
    else:
        print(1)
        print("账户不存在！")


# 查询逻辑
def bank_query(account, password):
    sql = "select * from bank where account=%s"
    param = [account]
    date = select_date(sql,param)
    if len(date) > 0:
        if password == date[0][2]:
            print("当前账号：",date[0][0])
            print("密码：*******" )
            print("当前余额:", date[0][7])
            print("当前居住地：", date[0][3],date[0][4],date[0][5],date[0][6])
            print("开户行中国工商银行")
        else:
            print("账号密码不正确！")
    else:
        print("账号不存在！")


#开户传入参数
def adduser():
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    money = float(input("请输入您的开户余额"))
    bankname= "中国工商银行"
    account = random.randint(10000000,99999999)
    status = bank_adduser(account,username,password,country,province,street,door,money)
    if status == 1:
        print("恭喜你开户成功下面是你的信息")
        # 每个元素都可传入%
        print(info % (account,username, country, province, street, door,money,bankname))
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
#存钱传入值
def  savemoney():
    account = input("请输入8位账号：")
    money = float(input("请输入存入的钱："))
    bank_savemoney(account,money)
#取钱传入值
def drawmoney():
    account = input("请输入要取钱的账号：")
    password = input("请输入账号密码：")
    money = float(input("请输入取出的金额"))
    bank_drawmoney(account,password,money)
#转账传入值
def transfer():
     account1 = input("请输入转出的账号：")
     account2 = input("请输入转入的账号：")
     password = input("请输入转出账号的密码：")
     money = float(input("请输入转出的金额："))
     if account1 == account2:
         print("转入转出账号相同，请重新输入不同账号")
     else:
         bank_transfer(account1,account2,password,money)
#查询传入值
def query():
    account = int(input("请输入账号："))
    password = input("请输入账号密码：")
    bank_query(account,password)


while True:
    chose=input("请选择业务")
    if chose == "1":
        print("开户")
        adduser()
    elif  chose == "2":
        print("存钱")
        savemoney()
    elif  chose == "3":
        print("取钱")
        drawmoney()
    elif  chose == "4":
        print("转账")
        transfer()
    elif  chose == "5":
        print("查询 ")
        query()
    elif  chose == "6":
        print("退出")
        print("bye")
        break