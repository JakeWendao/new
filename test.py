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

#