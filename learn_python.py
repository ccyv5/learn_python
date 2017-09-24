#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding=gbk                    使用中文注释必须添加

print("蔡朝勇开始学习python")
print("hello world")


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














