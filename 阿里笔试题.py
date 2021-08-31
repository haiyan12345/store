'''
编写一个函数，传入一个列表，并统计每个数字出现的次数。
返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
'''
"""使用for循环"""
num=[21,56,10,56,10,56,21,56,56,21,56,56,10,56,56]
num_dic={}
for item_str in num:
    if item_str not in num_dic:
        num_dic[item_str]=1
    else:
        num_dic[item_str]+=1
print(num_dic)

"""使用函数counter方法，可以迅速获取列表中元素的次数"""
from collections import Counter
arr=[21,56,10,56,10,56,21,56,56,21,56,56,10,56,56]
def counter(arr):
    return Counter(arr)
print(counter(arr))

"""使用list中的函数count，获取每个元素"""
a=[21,56,10,56,10,56,21,56,56,21,56,56,10,56,56]
def all_list(a):
    result = {}
    for i in set(a):
        result[i]=a.count(i)
    return result
print(all_list(a))