#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding=gbk                    使用中文注释必须添加

print("蔡朝勇开始学习python")
print("hello world")


######                  函数                     ######
print("函数")
print("函数调用")

print("常见的内置函数")
#http://www.cnblogs.com/sesshoumaru/p/6140987.html

print("函数定义")

# 使用def  定义函数  语法如下

# def func_name (  参数(没有类型哦) ) :           #注意冒号
#       缩进表示语句块

# 函数的return  没有写得时候默认 return None 简写 为 return
# 也可以return  特定值

print("pass  的使用 ，保证语法的正确")
#def nop():
#    pass            #什么也不做的语句
 
if True :
    pass               #没有pass 就会错误


print("应该检查 函数 的参数类型 是否符合要求")
#因为变量是可以随便换类型的

#通过函数 isinstance(变量，(类型，类型))
#判断 参数是否是需要的类型


def my_abs(num):
    if not isinstance(num ,(int,float)):        #如果 参数类型不是int  float
        print("type error")
        return
    if(num >0):
        return num
    else:
        return -num

print("调用 myabs")

my_abs("231")

#返回多个值 
def str_ab (str1,str2):
    return str2,str1       
#在return 时返回多个变量 ，用逗号隔开
    
s1 ="123"
s2 ="abd"
print(s1,s2)
s1,s2 = str_ab(s1,s2)
#接收 返回值时 直接 对应的 排列 赋值 即可
print(s1,s2)

#其实返回多值 是因为函数返回的 是一个tuple 
s3 = str_ab(s1,s2)
print(s3)       
#在语法上返回tuple 可以省略 括号，
#而多个变量 可以 同时接收一个 tuple 按位置赋值对应的 

#所以 python 的函数返回值时一个 tuple

#这时可以对tupel 进行修改吗
#可以按照tuple 访问key
print(s3[1])

print("难点 函数的 参数")
########        在 python 中，类型属于对象，变量是没有类型的：
a=[1,2,3]
a="Runoob"

# a是没有类型的，他只是一个 对象的引用 （一个指针）
# 可以指向 任意类型的 对象 "123",1,[1,2,3]
###可更改(mutable)与不可更改(immutable)对象
###在 python 中，strings, tuples, 和 numbers 是不可更改的对象
###而 list,dict 等则是可以修改的对象。

###不可变类型：  指向的空间的值没有变， 只是指针改变， 指向了新的空间
###     变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，
###     再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
###可变类型：    指向的空间的值被修改， 指针还是指向原来的空间
###     变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，
###     本身la没有动，只是其内部的一部分值被修改了。


# 不可变类型，指针变，可变类型，指针不变

#  python  的参数传递
#  不可变类型：类似 值传递， 将旧空间的 值 赋值给 新的空间，旧的空间不会被改变     新变量新指针
#   可变类型：类似指针传递，  新的空间  等于    旧的空间                           新变量旧指针
def abc(x):
    x[1]=   "蔡"
    return x
    
print("传入参数可变类型的")
a = [1,2,3]
print(a)
abc(a)      
print(a)        # a 的内容发生了变化


#       函数参数 有5种
#       参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

print("函数参数类型")
#       函数可以没有参数
def func_0():
    print("func_0   没有参数")
#       必选参数：  函数内部必选要使用的外部的参数

def func_1(v1):
    print("初始值 = ",v1)

    
def func_2(v1,v2=2,v3 =3):
    print("初始值 v1   = ",v1)
    print("初始值 v2   = ",v2)
    print("初始值 v3   = ",v3)
    
func_0()

c1 =10
print("函数定义     def func_1(v1):")
print("函数调用     func_1(c1)  c1 是必须参数，   调用函数是必须传入变量，或者值        ")
func_1(c1)    # func_1(10)  #   必选传入参数或者值

c1 ="a"
c2 ="b"
c3 ="c"
print("函数定义     def func_2(v1,v2=10,v3 =9):")
print("函数调用     func_2(c1)      c2,c3 是默认参数，调用时可以省略，函数内部直接使用默认值       ")
func_2(c1)   
print("函数调用     func_2(c1,c2)       ")
func_2(c1,c2)   
print("函数调用     func_2(c1,c2,c3)    ")
func_2(c1,c2,c3)   
#   目的是 修改函数可以 可以是之前的调用也可以使用  新增的变量，为默认参数 就可以
#   当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#   不按顺序调用  默认参数
print("函数调用     func_2(c1,v3 = c3,v2 = c2)    ")

func_2(c1,v3 = c3,v2 = c2)          #参数传入没有顺序，可以指定  传入参数       
#如果所有的参数都是 默认参数 ，则 可以不用写入参数

###############                     #bug  默认参数如果是 可变类型的list  tuple 则
###############                     #因为函数在定义时给 参数创建了一个空间，
                                    #不可变参数：重新创建一个空间
                                    #可变参数：  对这个空间，进行赋值。。空间还是不变
'''                                    
def add_end(L=[]):                  #       L 是一个可变的list 定义时 就创建了 一个 空间
    L.append('END')                 #       新增end元素
    return L                        #       返回 L 的地址
print(add_end())                    #
print(add_end())                    #       多次调用后   L的地址没有改变，值一直被改变
'''
###############                     #所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
'''
def add_end(L=None):                #原理     L   默认值   None 是一个不可变对象
    if L is None:                   #         L   如果是None             
        L = []                      #         L   重新赋值  空的list  (重新创建一个空间)
    L.append('END')                 #         L   增加 元素
    return L
print(add_end())
print(add_end())    

aaaa    =   [1,2,3,4]
print(aaaa)
print(add_end(aaaa))           #返回一个增加end 的新的list
print(aaaa)                     
print(add_end())
'''

#重点就是    不可变参数，，，值传递
#            可变参数       地址传递（默认的 可变参数  地址 定义后一直不变   ）

#########################                           ###     可变参数
#########################                           ###     可变参数的参数个数可以 任意个    
#########################                           ###     参数类型是可变的 list，tuple

#正常写太 复杂，，，，，在调用的实时需要 组装一个list 或者 tuple 传入
'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    numbers.pop()
    return sum
a = [1,2,3]
print(calc(a))      #   组装 list 传入
print(a)            #   测试   参数是可变类型，，就是地址传递
'''
def func_3(*numbers):       #添加 * 后  numbers  一直接收一个 tuple 的参数。。内容实时固定。
    sum = 0
    for n in numbers:       #遍历赋值   
        sum = sum + n * n  
    return sum
a = [1,2,3,4,5]
print(func_3())             #可以选择 传入多少个数的 参数传入没有顺序，可以指定
print(func_3(1,2,3))        #只能一个元素一个元素 排队 传入（理解 就是  重新定义一个tuple ）
print(func_3(a[0],a[1],a[2],a[3],a[4]) )
#简单方法
print(func_3(*a))           # 理解  * 的功能可以 就是把 list 或者 tuple 转换成 tuple 。



#######################                               #关键字参数

#因为可变参数的存在      函数调用时自动组装成一个 tuple。
#关键字参数就是可以      函数调用时自动组装成一个 dirt  重点就是
#将自动传入的 参数 内容 和对应的 参数名  匹配 生成   字典 dirt

def func_4(**sss):
    print(sss)
func_4()        #空字典
func_4(  key1="value1" )   
func_4(  key1="value1",key2="value2"         )   
#关键字参数有什么用？它可以扩展函数的功能。
#比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
#试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

d={ "key1":"v1","key2":"v2" ,"key3":"v3"}           
func_4(  key1=d['key1'],key2="v2"         )     #g给参数名  赋值的方式 组装字典

func_4(**d)            #因为知道  d 是字典  可以 直接传入     只是拷贝字典，，，不影响外部 字典内容        


#命名关键字参数

#因为可以随意的传入字典，，，但是函数内部不知道 到底是什么。
#可以 事先 在函数内部 检查关键字  来判断 需要的关键字 是否 传入函数


def func_5(**sss):
    if  'key4' in sss :                  #通过in 功能确定 改关键字 在 传入的 字典中
        print("key 4 存在")   
    print(sss)                                              # in 功能
    
d2 =   {"key1":"v1","key2":"v2","key3":"v3","key4":"v4"}
func_5(**d2) 


#命名 关键字参数
#但是我们还是可以随意传入我们不知道的 关键字 内容实时内容
# 我们可以   限制 传入的  关键字 名          只接受固定的关键字 参数       
#########################################################            #通过单独的   *，  表示后面的都是关键字
#########################################################            #如果前面有一个 可变参数 *s,  则后面可以直接跟 关键字
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')                   # 必须传入 参数名
  
#d2= {"sdas":"aaa","city":"123","job":"456"}                         #关键字 需要完全相同
d2= {"city":"123","job":"456"}                                       #通过简单 方法调用 关键字参数，
person('Jack', 24, **d2)                                             #必须保证外部字典包含的关键字，和定义的关键字完全相同

#关键字  参数 可以设置默认字，           设置值 之后 可以  缺省 这个关键字

#def person(name, age, *args, city, job):
#   print(name, age, args, city, job)

############                                        一定要注意  * 的存在  没有可变参数 *s，就必须要有一个 ,*, 来确定位置




def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
f1(1, 2)
#a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
#a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)
#a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
#                                                   最神奇的是通过一个tuple和dict，你也可以调用上述函数：
print("##################")

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c)
    print(d)
    print('kw =', kw)
args = (1, 2,3,4,5,6)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
#a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2,3)                                     # 不存在可变参数，  没key参数只能保存  3个
kw = {'d': 88, 'x': '#'}                            #  d 在 函数  不是字典  保存的
f2(*args, **kw)
#a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
#################所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

###################################################
###################################################
###################################################         理解 func(*args, **kw)
###################################################         前面 安装tuple 给参数一个一个赋值，后面则对应的 字典拷贝    
###################################################         参数 按照参数定义 赋值，引用    按照关键字定义 拷贝
###################################################
###################################################
###################################################
######                  函数                     ######



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














