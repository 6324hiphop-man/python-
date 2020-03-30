# -*- coding: utf-8 -*-

'''name = "Hape"
yearsold = 18
s1 = "%s's yearold is %3d"%(name,yearsold)
print(s1)'''


'''name = "Hape"
yearsold = 18
s1 = "{0}'s yearsold is {1:3}".format(name,yearsold)
print(s1)'''


'''d1 = {"name":"Hape","room":"717","IQ":"70","type":"就是个智障"}
d2 = "Hi！WTF"
s1 = "{0},姓名：{name},宿舍：{room},智商:{IQ},{type}".format(d2,**d1)
print(s1)'''


'''s1 = "姓名：{name:10} \n宿舍：{room} \n智商:{IQ} \n类型：{type}".format(name='Hape',room=717,IQ='70',type='就是个哈皮')
print(s1)'''

'''s1 = ['关爱','WTF','小朋友','生长健康']
s2 = "{}{}{}{}".format(s1[3],s1[1],s1[0],s1[2])  #format(*s1)
print(s2)'''

'''x = 123
s = "{}的二进制形式是：{:0>8b}".format(x,x)
print(s)'''
 

'''x = 123
s = "{}的十进制形式是：{:d}".format(x,x)
print(s)'''

'''x = 123
s = "{}的十六进制形式是：{:x}".format(x,x)
print(s)'''

x = 123
s = "{}的八进制形式是：{:o}".format(x,x)
print(s)