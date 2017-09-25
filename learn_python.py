#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding=gbk                    使用中文注释必须添加

print("蔡朝勇开始学习python")
print("hello world")



"""
######                  dirt                     ######
print("dirt")
#字典  里面的元素是 key-value 
#原因是  输入key之后就知道了 存放value 的内存地址，直接找到了
#所以比list 查找要快许多
#一个key只能对应一个value 
print("key是不可变对象")
print("value是可以修改的")
print("字典的输出话用花括号")
d = {   'a':1,'b':2,'c':'蔡'  }
print(d)
print("只能通过key来访问value")
print(d['c'])
print("将value 变成list")
d['c']=["蔡","超","勇"]
print(d)
d['c'].pop()    
print(d)
#list的操作 list.append("123")   list.pop()     list.pop(2) list.insert(2) 

print("key 是可不怕的那么 tuple 是否可以做 key 有list的 tuple 是否可以是key")

d   = {1:1,"a":2,(2,3,4):3}
print(d)
print("访问key tuple")
print(    d[1]  )
#访问字典中的 以tupel 为key 的value 时，[必须是完整的key]
print(    d[2,3,4]   )

#d   = {1:1,"a":2,(2,3,[1,2,3]):3}      #语法错误
#print(d)

print("dirt 中的 key 是不可变对象，只能用不可变的数据类型，数组，字符串，没有list的tuple")

print("通过in 访key 是否存在，结果返回 True 或者 False")
d   = {1:1,"a":2,(2,3,4):3}

print(  "a" in d )
print(  (2,3,4) in d) 

#print("通过 dirt 通过的 get 方法 访问key ，不存在返回None 或者直接指定的 value")

print( d.get(1))
print( d.get(2))
print( d.get((2,3,4)))
#print("如果不存在，返回-100")
print( d.get(2,-100))

#print("删除一个key，使用d.pop(key) ")
print(d)
d.pop(1) 
print(d)
print("内部是无序的")

#print("增加一个key，直接 写 d[newkey]   =   newvalue ")
print(d)
d[222]="sss"
print(d)

######                  dirt                     ######


######                  set                     ######
print("set")
print("set 是一个内部没有 value 的字典。只保存了 key")
print("因为key 是不可能重复的，所以 set 里面没有重合的key   ")
print("set 用来做交集和并集和 处理，可以计算 不同key的个数")
print("set 的使用就像一个 函数一样，在定义的时候 通过一个list 的list 内的元素 传入set内部。")
print("set 内部就用了 三个元素 是没有顺序的")
#print("s  =set(list)      ")
s = set(    [1,2,3]  )
print(s)
#print("如果list是空的呢！")
s= set([])
print(s)

s = set(    [1,2,3,3]  )    #自动过滤 重复key
print(s)
#print("s.add(key)增加新的key")
s.add(5)
print(s)
#print("s.remove(key)删除key")
s.remove(3)
print(s)

s1 = set([1,2,3,4])
s2 = set([4,5,6,7])

#print("set 的交集和并集")
s3  =   s1&s2
s4  =   s1|s2
print(s3)
print(s4)

print("不可变对象")

print("list 是可变得  ")
a = ['c', 'b', 'a']
print(a)
#print("将 list a 中 安顺序排放")
a.sort()                            #list.sort() 排序函数
print(a)

print("字符串 是可变得  ")

a = "addsadaaaf"
print(a)
a.replace("a","A")                  #str.replace（"a","A"）字符串替换函数    
b= a.replace("a","A")               #生成新的字符串 ，原来的字符串不会改变
print(a)
print(b)

######                  set                     ######
"""

"""
######                  循环                     ######
print("循环")
#while 
print("while")
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
else:           #while 还可以使用 else哦
    print(n)
print(sum)
#for 
print("for")
#将 序列中的 元素 逐一赋值给    x
mytuple =   (1,2,3)
for x in mytuple:   
    print(x)

#生成 有序序列list

for_sum =   0;
for x in [1,2,3,4,5]:   
    for_sum=    for_sum +x;
print(for_sum)
for_sum =   0;
for x in range(2,5):        
#range 函数生成一个带起点和终点的有序序列   
    for_sum=    for_sum +x;
print(for_sum)

######                  循环                     ######
"""

"""
######                  条件判断                     ######
'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''
print("条件判断")
#注意点 input 输入的是str 
#通过int 函数  将 字符串转换成 整数转换字符
s = input('birth: ')
print(s)
birth = int(s)    #输入错误会error
print(birth)
if birth < 0:
    print('负数')
else:
    print('正数')
######                  条件判断                     ######
"""

"""
######                  list和tuple                     ######
print("list和tuple")

#list 是数据类型， list的一种有序的集合，可以随时添加和删除和修改元素
mylist  =   ['abc','efg','hij']
print(mylist)
print("mylist   len = ",len(mylist))

#通过索引访问 list
print("通过顺序索引访问 list")
print("mylist[0]= ",mylist[0])
print("mylist[1]= ",mylist[1])
print("mylist[2]= ",mylist[2])
print("通过逆序索引访问 list")
# -1 就是list的最后一个
print("mylist[-1]= ",mylist[-1])
print("mylist[-2]= ",mylist[-2])
print("mylist[-3]= ",mylist[-3])

print("注意正反越界 list")

#给list最后添加元素
print("给list最后添加元素")
mylist.append('123')
print(mylist)

#给list指定位置添加元素
print("给list指定位置添加元素")
mylist.insert(3,'ABC')
print(mylist)

#给list最后删除元素
print("给list最后删除元素")
mylist.pop()
print(mylist)

#给list指定位置删除元素
print("给list指定位置删除元素")
mylist.pop(1)
print(mylist)

#给list指定位置元素替换元素
print("给list指定位置元素替换元素")
mylist[0]= "蔡朝勇"
print(mylist)

#list的元素而可以是list 二维数组
#类似二维数组
print("list的元素而可以是list 二维数组")
mylist[0]= ['蔡','朝','勇']
print(mylist)
print("mylist[0][2]= ",mylist[0][2])
mylist.pop()
mylist.pop()
mylist.pop()
#list  可以定义空的
#mylist = [] 
my_null_list = [] 
print(my_null_list)


#tuple 有序列表  元组 初始化后元素的指向无法改变
mytuple =   (1,2,3)
print("mytuple",mytuple)

#访问方式  和 list 相同
print("通过顺序索引访问 tuple")
print("mytuple(0)",mytuple[0])
print("mytuple(1)",mytuple[1])
print("mytuple(2)",mytuple[2])
print("通过反序索引访问 tuple")
print("mytuple(-1)",mytuple[-1])
print("mytuple(-2)",mytuple[-2])
print("mytuple(-3)",mytuple[-3])

my_null_tuple = ()
print(my_null_tuple)
#错误，歧义
my_one_tuple  = (1)
print(my_one_tuple)
my_one_tuple  = (1,)
print(my_one_tuple)

print("可变tuple-list")
mytuple_list   = (1,2,3,4,['a','b','c','d'])
print(mytuple_list)
mytuple_list[4][0]  =   '蔡'
print(mytuple_list)







print("")
######                  list和tuple                     ######


######                  字符串                     ######

#记住同意使用utf-8编码
print("字符串")

#ord 字符转换整数 函数
#chr 整数转换字符 函数
print   (    ord('A')   )
print   (    ord('蔡')   )
print   (    chr(ord('A'))   )
print   (    chr(ord('蔡'))   )

#len 字符串长度计算 函数 
myname  =   "蔡朝勇"
print   (myname)
print   ("myname len =",len(myname))

#格式化输出
#"%d" % (num)
print   ("myname len = %d over len= " % (len(myname)),len(myname))
#   %d      整数
#   %f      浮点数
#   %s      字符串
#   %x      十六进制整数
#   %.2f    显示2为小数
######                  字符串                     ######
"""


""" #多行注释
######                  输入与输出                     ######
#输出
print("输入与输出")
#输出多个字符串
print('123','456','789')
#逗号会变成 空格出书

#输出整数
print(100+200)

#输入
#name = input()                     #该函数获取的是一个字符串
#name = input('please enter your name: ')   #该函数提供一个字符串提醒
#print("name=",name)
######                  输入与输出                     ######

######


######                  注意点                         ######
#'#'注释
#':'语句结束
#'缩进'语句块
#tab应该这是4个空格的缩进
#python 区分大小写
######                  注意点                         ######


######                  数据类型和变量                 ######



######                  数据类型和变量                 ######
print("数据类型和变量")
#整数      1 2 3
#浮点数    0.000123    1.23e4
#字符串    "abcdefg"

#字符串中的转义字符
print("ccyv5\'ccyv5")

#不许转义功能       r""
print(r"ccyv5'ccyv5")

#多行显示   \n
print("ccyv5\nccyv6")

#多行显示'''...'''
print('''ccyv7
ccyv8
ccyv9''')

#布尔值
#   True False
print(True)
print(False)

#   and or not 运算
print("True and True")
print(True and True)
print("True and False")
print(True and False)
print("not   True")
print(not   True)
print("False or False")
print(False or False)
print("True  or False")
print(True  or False)

#空值 None    不是0
print(None)

#变量
#变量的类型 是随时可以变化的，反复赋值变更新的类型
#值是在内存中的，变量相当于指针，指向内存
a = 1
print("a= ",a)
a="a_str"
print("a= ",a)
a=True
print("a= ",a)
a=None
print("a= ",a)

#常量
#没有真正意义上的常量
#以 全部大写命名 常量

#除法 俩种除法

#整数除 
print(10//3)
#取余数
print(10%3)
#浮点数除
print(10/3)

######                  数据类型和变量                 ######
"""














