'''
小明去超市购买水果，账单如下
苹果  32.8
香蕉  22
葡萄  15.5
'''
info1={"苹果":32.8,"香蕉":22,"葡萄":15.5}
'''
小明，小刚去超市里购买水果
小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，
请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
以姓名做key，value仍然是字典
'''
friuts = {"苹果":12.3,"草莓":4.5,"香蕉":6.3,"葡萄":5.8,"橘子":6.4,"樱桃":15.8}# 水果和单价
info = {
    "小明": {"fruits":{"苹果":4, "草莓":13,"香蕉" :10},  #水果和斤数
    "money":0
    },
    "小刚": {"fruits": {"葡萄":19,"橘子" :12, "樱桃":30},
    "money":0
    }
}

def money(f, i):
    moneys = 0
    for key in i["fruits"].keys():
        moneys += f[key] * i["fruits"][key]
    i["money"] = moneys


name = input("请输入要计算的人名：")
money(friuts,info[name])
print(info[name])