# !/usr/bin/env python
# -*-coding:utf-8-*-
# author:jakewendao
#
# 1.有1,2,3,4这4个数字，问组成多少个互不相同且无重复数字的3位数？都是多少？
#分析：先排后去重
# count = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i != j) and (i != k) and (k != j):
#                 print int(str(i)+str(j)+str(k))
#                 count = count + 1
# print count

# 2.企业发奖金根据利润的不同来划分提成比例。
#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
#利润高于10万元，低于等于20万，高于10万元的部分可提成7.5%；以此类推。
#分析，划分阶段，利用阶乘联系起来各阶段(比如bonus2 = bonus1 + 100000*0.075)，然后各阶段计算阶段中最大(全部)的提成。
# bonus1 = 100000 * 0.1
# bonus2 = bonus1 + 100000*0.075
# bonus4 = bonus2 + 200000*0.05
# bonus6 = bonus4 + 200000*0.03
# bonus10 = bonus6 + 400000*0.015
# i = int(raw_input(u"请输入您的收入金额\n"))
# if i <= 100000:
#     bonus = i * 0.1
# elif i<= 200000:
#     bonus = bonus1 + (i-100000)*0.075
# elif i<= 400000:
#     bonus = bonus2 + (i-200000)*0.05
# elif i<= 600000:
#     bonus = bonus4 +(i-400000)*0.03
# elif i<= 1000000:
#     bonus = bonus6 + (i - 600000)*0.015
# else:
#     bonus = bonus10 + (i - 1000000)*0.01
# print int(bonus)
# 3、一个整数，它加上100是完全平方数，它加上268是另外1个完全平方数，请问该数是多少。
# 分析：首先，我们考虑在10万范围内遍历，不然可能会内存溢出。然后考虑开方后的结果再相乘来跟原来的数字进行比对。
# import math
# for i in range(100000):
#     x = int(math.sqrt(i+100))
#     y = int(math.sqrt(i+268))
#     if (x*x == i +100) and (y *y == i +268):
#         print "这个整数就是",i
# 4、输入年月日，就计算出这天是这一年的第几天
# 分析：使用switch case来匹配对应的月，然后计算闰年来增加3天。
# year = int(raw_input(u"请输入年"))
# month = int(raw_input(u"请输入月"))
# day = int(raw_input(u"请输入日"))
#因为python中没有switch case，所以自己定义函数，是借鉴别人的做法。
# def foo(var):
#     return {
#         1: 0, 2: 31, 3: 59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334
#     }.get(var,'error')
# # print foo(2)
# sum_month_day = int(foo(month)) + day
# if (year % 400 == 0 ) or ((year % 100!=0) and (year % 4 == 0)):
#     if (month >2):
#         sum_month_day = sum_month_day + 1
# print sum_month_day
# 5、3个整数排序，从小到大。
# 分析：x与y比较，较小的放在x上，x与z比较，较小的放在x上，保证x最小，然后y跟z比较，较小的放在y上，确定排序。
# 也可以使用sort()，官方的排序。
#下面是对1个列表进行排序，然后对列表进行倒序。
# I = [2,8,1]
# I.sort()
# I1 = []
# length = len(I)
# for i in range(length-1,-1,-1):
#     I1.append(I[i])
#     print i
# print I1
#下面是进行解题。
# str = raw_input(u"请输入您的3个数字，中间空格隔开\n")
# list1 = str.split(' ')
# x = int(list1[0])
# y = int(list1[1])
# z = int(list1[2])
# someone = 0
# if (x<y):
#     pass
# else:
#     someone = x
#     x = y
#     y = someone
# if (x<z):
#     pass
# else:
#     someone = x
#     x = z
#     z = someone
# if (y<z):
#     pass
# else:
#     someone = y
#     y = z
#     z = someone
# print type(x),y,z

# 增加示例：有时需要将list以str的形式输出
# ",".join(list_sample)  比如下面的
# a_list = ["h","e","l","l","o"]
# print ",".join(a_list)
# 但是有时，列表里是数字，那么需要先把数字改为字符串。
# num_list = [0,1,2,3,4,5,6,7,8,9]
# num_list_new = [str(x) for x in num_list]  #这一行还可以用num_list_new = map(lambda x:str(x), num_list)
# print type(",".join(num_list_new))
#想把list里面的str变为int，可以用下面的方法，仅适用于python2
# num_list = ['0','1']
# num_list_new = map(eval, num_list)
# #python3中需要这么用
# ls=[1,2,3]
# rs=map(str,ls)
# print(list（rs）)
# # 6、用*号输出字母P的图案
# print 'Hello Python World!\n'
# print '*'*10
# for i in range(5):
#     print '*        *'
# print '*'*10
# print '*\n'*6
# # 7、输出特殊图案
# a = 176
# b = 219
# print chr(b),chr(a),chr(a),chr(a),chr(b)
# print chr(a),chr(b),chr(a),chr(b),chr(a)
# print chr(a),chr(a),chr(b),chr(a),chr(a)
# print chr(a),chr(b),chr(a),chr(b),chr(a)
# print chr(b),chr(a),chr(a),chr(a),chr(b)
# 8、输出9*9口诀
# for i in range(0,10):
#     for j in range(1,i+1):
#         print i,'*',j,' ',
#     print '\n',


