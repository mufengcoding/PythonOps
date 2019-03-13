#学习编程的一定会学的语句
```
from lufeipython.Chapter1.user_input import name

print("hello Python！")
```

2+2是表达式也称为归约

2**2即2的2次方，也是表达式运算优先级最高的

%取余数

有趣的是python的除法

三个除法的概念 传统除法/精确除法/地板除法

1、传统除法：整数相除结果是整数，浮点数相除结果是浮点数

2、精确除法：无论操作数是整数还是浮点数，得到的商总是真实结果，总是得到浮点数

3、地板除：无论操作数是整数还是浮点数，得到的商不保留浮点数的尾数

在python2.6版本中4/2是等于2的 只有3版本的时候结果是2.0


### 数据类型

1.整型（int）

2.浮点型（float）

3.字符串

*用于字符串的时候表示复制  只能用于字符串和数字，不能用str*str
 
比如"li"*5输出 "lilililili"

变量名区分大小写

整数可以与浮点型的值相等

round 函数四舍五入取值


### 布尔型

值只有True/False 

小写的会报错

比较操作符 比较两个值，求值为一个布尔值

布尔操作符

and 与 or 或 not 非 需要注意的话 这边和javascript以及其他部分语言有区别  || && !

### 操作流的元素

操作流的元素开始部分通常为"条件"，接下来是一个代码块
```
passwd: str = input()

if name == "mufengs":
    print("hello mufengs")
if passwd == "233":
    print("access granted")
elif passwd == "234":
    print("good")
else:
    print("wrong passwd")
```
### while 语句

### break 语句

###continue语句

像break一样，continue语句在while语句内部执行

###for循环和round()函数

代码执行有限次数的时候选用 当然也有办法用while实现

类真类假的值可以让代码的可读性增强


等价于for的while循环方式
```
print('my name is')
o = 0
while o < 5:
    print('Jimmy Five Times(' + str(o) + ')')
    o = o + 1
```

range()的开始/结束/步长

如 range(0,10,2)

### from import 语句

如from random import *


用sys.exit()提前结束程序

## 第二章习题

等于操作符和赋值操作符的区别是什么

==是等于操作符，它比较两个值，求值为一个布尔值，而=是赋值操作符将值保存在变量中

Round函数返回一个数值,该数值是按照指定的小数位数进行四舍五入运算的结果

abs() 函数返回数字的绝对值。

## 第三章函数

def() 参数是变元也就是其他语言中的变量

### 3.3 None值
在python中有一个值为None，他表示没有值
```
a = print("1111")

print(a)
```

上面的例子可以明确的看出来 print是不可以参与值的赋值运算的
```
print("23", end="...")
print("456")
```

23...456 #修改默认换行的
````
print('cats', 'dogs', 'mice', sep="...")
````
cats...dogs...mice sep表示修改默认的分割符号，默认是空格


### 3.5 局部变量不能在全局作用域下使用
如下例子所示
```
def spam():
     eggs = 31337
spam()
print(eggs)
```
```
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'eggs' is not defined
```

### 3.6 global语句

如果想在一个函数中修改全局变量中的存储的值，就必须对该变量使用global语句

### 3.7 异常处理
try和except语句
如下面的try

## 第三章小姐

函数是将代码逻辑分组的主要方式

## 第四章列表
列表是一个值，它包含多个字构成的序列

在一个切片中，第一个整数是切片开始处的下标，第二个整数是切片结束处的下标

列表多重赋值

变量的数量和列表的长度必须严格相等，否则出现ValueError

````
cat = ['name', 'age', 'weight']
name, age, weight = cat
````

类似列表 字符串和元组

元组 tuple (1,2,3)

列表 list [1，2，3]

###copy()和deepcopy()
copy()可以用来复制列表和字典这样的可变值，而不只是复制引用

如果复制列表中包含列表，就需要使用copy.deepcopy()这个函数来代替



## 第五章 字典和结构化数据
字典类似与列表，但是没有下标

可以参考js的对象，区别是调用的时候一个用. 一个用[]

键值对输入的顺序不重要和列表的区别，列表的顺序是重要的

## 第六章 字符串操作

多行注释可以使用 """    """


1.程序设计和数据结构
2.处理命令行参数


## 第七章 模式匹配与正则表达式

强口令检测
