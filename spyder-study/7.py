# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:33:53 2020

@author: George~
"""
#定义判断闰年函数
#函数参数：year————被判断年份
#函数值：是闰年返回True，不是闰年返回False


def isleap(year):
    if year%4==0 and year%100!=0 or year%400==0:    #“能整除4的但不能整除100” 或 “能整除400” 算法1
        return True
    else:
        return False
    
    
    
year = int(input("请输入年份："))
if isleap(year):
    print("{}is a leap".format(year))
else:
    print("{}is not a leap".format(year))
    