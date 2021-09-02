import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")

bank={}
"""
{"张三":{ "account":12345678, "country":"中国"},
        "李四":{}}
"""

bank_name="工商银行七马路分行"   #全局变量

#一一对应  ，  不是名称对应
def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >= 100 : return 3#bank_adduer=3
    if account in bank : return 2#bank_adduer=2
    bank[account]={
        "uesrname": username,
        "password": password,# password = input("请输入您的密码")
        "country": country,#country = input("\t\t请输入您的国家")
        "province": province,
        "street": street,
        "door": door,
        "money":0,
        "bank_name":bank_name
    }
    return 1   #bank_adduser=1
# 存钱逻辑
def bank_savemoney(account,money):
    if account in bank.keys():
        bank[account]["money"] = bank[account]["money"] + money
        print("卡内余额：", bank[account]["money"])
    else:
        print(False)
        print("账号不存在")
# 取钱逻辑
def bank_drawmoney(account,password,money):
    if account in bank.keys():
        if password == bank[account]["password"]:
            if money <= bank[account]["money"]:
                bank[account]["money"] = bank[account]["money"]-money
                print("成功取出金额：",money)
                print("账户余额：",bank[account]["money"])
            else:
                print(3)
                print("当前余额不足！")
        else:
            print(2)
            print("账户密码错误")
    else:
        print(1)
        print("账号不存在！")
#转账逻辑
def bank_transfer(account1,account2,password,money):
    if account1 in bank.keys():
        if  password == bank[account1]["password"]:
            if  account1 in bank.keys():
                if money <= bank[account1]["money"]:
                    bank[account1]["money"] = bank[account1]["money"] - money
                    bank[account2]["money"] = bank[account2]["money"] + money
                    print("转出账户余额为：",account1)
                    print("转入账户余额为：", account2)
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
#查询逻辑
def bank_query(account,password):
    if account in bank.keys():
        if password in bank[account]["password"]:
            print("当前账号：", account)
            print("密码：*******", )
            print("当前余额:", bank[account]["money"])
            print("当前居住地：", bank[account]["country"], bank[account]["province"],
                  bank[account]["street"], bank[account]["door"])
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
    account = random.randint(10000000,99999999)
    status = bank_adduser(account,username,password,country,province,street,door)
    if status == 1:
        print("恭喜你开户成功下面是你的信息")
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
        # 每个元素都可传入%
        print(info % (account,username, country, province, street, door, bank[account]["money"], bank_name))
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
#存钱传入值
def  savemoney():
    account = int(input("请输入8位账号："))
    money = int(input("请输入存入的钱："))
    bank_savemoney(account,money)
#取钱传入值
def drawmoney():
    account = int(input("请输入要取钱的账号："))
    password = input("请输入账号密码：")
    money = int(input("请输入取出的金额"))
    bank_drawmoney(account,password,money)
#转账传入值
def transfer():
     account1 = int(input("请输入转出的账号："))
     account2 = int(input("请输入转入的账号："))
     password = input("请输入转出账号的密码：")
     money = int(input("请输入转出的金额："))
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
        break

