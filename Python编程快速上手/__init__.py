# 学习编程的一定会学的语句
from lufeipython.Chapter1.user_input import name

print("hello Python！")
# 2+2是表达式也称为归约
# 2**2即2的2次方，也是表达式运算优先级最高的

# %取余数
# 有趣的是python的除法
# 三个除法的概念 传统除法/精确除法/地板除法
# 1、传统除法：整数相除结果是整数，浮点数相除结果是浮点数
# 2、精确除法：无论操作数是整数还是浮点数，得到的商总是真实结果，总是得到浮点数
# 3、地板除：无论操作数是整数还是浮点数，得到的商不保留浮点数的尾数
# #在python2.6版本中4/2是等于2的 只有3版本的时候结果是2.0


# 数据类型

# 1.整型（int）
# 2.浮点型（float）
# 3。字符串

# *用于字符串的时候表示复制  只能用于字符串和数字，不能用str*str
# 比如"li"*5输出 "lilililili"

# 变量名区分大小写

# 整数可以与浮点型的值相等

# round 函数四舍五入取值


# 布尔型
# 值只有True/False
# 小写的会报错
# 比较操作符 比较两个值，求值为一个布尔值
# 布尔操作符
# and 与 or 或 not 非 需要注意的话 这边和javascript以及其他部分语言有区别  || && !

# 操作流的元素
# 操作流的元素开始部分通常为"条件"，接下来是一个代码块

passwd: str = input()

if name == "mufengs":
    print("hello mufengs")
if passwd == "233":
    print("access granted")
elif passwd == "234":
    print("good")
else:
    print("wrong passwd")

# while 语句

# break 语句

# continue语句
# 想break一样，continue语句在while语句内部执行

# for循环和round()函数
# 代码执行有限次数的时候选用 当然也有办法用while实现
# 类真类假的值可以让代码的可读性增强


# 等价于for的while循环方式

print('my name is')
o = 0
while o < 5:
    print('Jimmy Five Times(' + str(o) + ')')
    o = o + 1
# range()的开始/结束/步长
# 如 range(0,10,2)

# from import 语句
# 如from random import *


# 用sys.exit()提前结束程序

# 第二章习题
# 等于操作符和赋值操作符的区别是什么
# ==是等于操作符，它比较两个值，求值为一个布尔值，而=是赋值操作符将值保存在变量中

# Round函数返回一个数值,该数值是按照指定的小数位数进行四舍五入运算的结果
# abs() 函数返回数字的绝对值。
