# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:29:30 2020

@author: George~
"""
import datetime
st = datetime.datetime.now()      #获取时间

second = st.second

print("{}年{}月{}日 {}时{}分{}秒".format(st.year,st.month,st.day,st.hour,st.minute,st.second))
print(second)




