'''def immutabledemo(a):
    if a>0:
        a=-1
    else:
        a=1
    return

x = float(input("输入一个负数："))
immutabledemo(x)
print(x)
x = float(input("输入一个正数："))
immutabledemo(x)
print(x)'''


'''def mutable(la):                #形式参数为列表
    i=0 
    while i<len(la):            #通过遍历法江列表的每个元素加5
        la[i]=la[i]+5
        i+=1
    return
ll=[1,2,3,4,5]                  #定义一个列表
mutable(ll)                     #将上述列表作为实际参数调用函数
for i in ll:                   #循环输出列表中的所有元素
    print(i,end=' ') '''

'''def istriangle(b1,b2,jiajiao):
    if jiajiao<0 or jiajiao>180:
        return False
    else:
        return True
b1 = float(input("请输入边长1："))
b2 = float(input("请输入边长2："))
b3 = float(input("请输入夹角："))
if istriangle(b1,b2,b3):
    print("%.3f %.3f %.3f 构成三角形"% (b1,b2,b3))
else:
    print("%.3f %.3f %.3f 不构成三角形" % (b1, b2, b3))'''

def do_plus(x,y):
    a=x+y
    return
x = int(input("x="))
y = int(input("y="))
a=x+y
print("a=%d"% a)
