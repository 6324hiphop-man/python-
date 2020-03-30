# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 23:44:52 2019

@author: George~
"""

import time      #导入内置模块


totaltime = eval(input("请输入倒计时总时间："))                                    #通过内置函数input（）输入设定秒数，通过eval（）转换为数值
total = totaltime

print("{}秒开始倒计时".format(totaltime).center(20,'-'))                          #提示开始

st = time.time()                                                                  #获取当前时间

#通过循环实现倒计时
for n in range(totaltime+1):
    finish='>'*(totaltime-n)                                                      #原字符
    re='<'*n                                                                      #倒计时取代字符
    print("\r{}{}\t{}".format(finish,re,total),end='')                            #格式化输出实现倒计时
    if total==0:                                                                  #倒计时到0退出循环
        break
    time.sleep(1)                                                                 #延时1秒
    total-=1                                                                      #每秒减1
    
print("\n"+"{}秒倒计时结束".format(totaltime).center(20,'-'))                      #提示结束

et=time.time()                                                                     #获取结束时间以计算总时间
print("误差：{:.3f}%".format((et-st)/100))                                         #计算误差率并格式化输出     

