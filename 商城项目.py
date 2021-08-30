'''
    1.用金钱
    2.空的购物车
    3.有足够商品
    4.正常购物
        是否有这个商品
        金钱是否足够
            添加购物车

    技术选型：
        1.判断
        2.循环
        3.容器技术
        4.输入input
        5.打印
    任务1：
        10张联想优惠券，0.5
        20张老干妈优惠券：0.6
        10张乌江榨菜优惠券，0.9
    最后使用优惠券来结算。
'''
# 1.准备一个商品柜
import time
import random
#1.1优惠券
num=random.randint(1,40)
print(num)
print("---温馨提示：购物打折有大额优惠券！--")
a=input("请输入是否要优惠券,0不要，1要")
a=int(a)
if a==0:
    print("不要优惠券！")
else:
    if a ==1:
        print("随机抽取一张优惠券")
        if num >= 30 :
            b= 0.5
            print("您抽到的优惠券是联想优惠券1张打五折",b)
            b = int(b)
        elif num <= 10:
            b=0.6
            print("您抽到的优惠券是老干妈优惠券1张打六折",b)
            b = int(b)
        else:
            b=0.9
            print("您抽到的优惠券是乌江榨菜优惠券1张打九折",b)
            b = int(b)
shop = [
    ["联想电脑",4500,],
    ["Mac Pc",12000,],
    ["HUA WEI WATCH",1200,],
    ["海尔洗衣机",5000,],
    ["卫龙辣条",3.5,],
    ["老干妈",15,],
    ["乌江榨菜",1.5,]
]
# 2.准备钱包
money = input("请初始化您的余额：")
money = int(money)


# 3.空格购物车
mycart = []

# 4.正常买东西

while True:
    # 展示商品
    for key,value in enumerate(shop):
        print(key,value)
    # 买东西
    chose = input("请输入您要的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        #  这个商品是否存在
        if chose > len(shop)or chose < 0: # len(shop) = 7
            print("该商品不存在！别瞎弄！请重新输入：")
        else:
            # 如果有该商品的优惠券 1使用优惠券 2看钱够不够
            if a==0 and money < shop[chose][1]:
                print("对不起，您的余额不足，穷鬼，请到其他地方购买！")
            elif a==1 and money < ((shop[chose][1])*b):
                print("对不起，即使使用优惠券余额也不足")
            else:
                if a==0:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    print("恭喜，添加购物车成功！您的余额还剩：",money,"!")
                elif a==1:
                    mycart.append(shop[chose])
                    if b==0.5 and chose==0:
                        money = money - ((shop[chose][1]) * 0.5)
                        print("已使用一张优惠券")
                        print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
                    elif b==0.6 and chose==5:
                        money = money - ((shop[chose][1]) * 0.6)
                        print("已使用一张优惠券")
                        print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
                    elif b==0.9 and chose==6:
                        money = money - ((shop[chose][1]) * 0.9)
                        print("已使用一张优惠券")
                        print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
                    else:
                        money=money-shop[chose][1]
                        print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("输入非法！别瞎弄！请重新输入：")

# 结算,打印购物小条
print("以下是您的购物小条，请查收：")
print("----------------------------")
for key,value in enumerate(mycart):
    print(key,value)
print("您本次余额还剩：￥",money)
print("----------------------------")


































