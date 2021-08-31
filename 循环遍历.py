dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key
# for key,value in dict:
#     print(key,value)
for i in dict.keys():
    print(i)
for a in dict:
    print(a)
#2、请循环遍历出所有的value

for i in dict.values():
    print(i)
for a in dict:
    print(dict[a])
# 3、请在字典中增加一个键值对,"k4":"v4"
dict["k4"]="v4"
print(dict)

# del dict ["k1"]     #通过key删除key-value
# print(dict)
# dict["k1"]="k0"      #通过key修改key-value
# print(dict)
# print("k3" in dict)  #通过key查询key-value