# 变量名随意只要不以数字开头，然后尽量有意义  一般使用驼峰和_开头
print("hello Python3.7")

print("what's your name?")

_name = input()
print("it's nice to meet you", _name)
_len = len(_name)
print("this my name length:")
print(_len)
print("what's your age")
_age = input()
print("you will be " + str(int(_age) + 1) + ' in a year!')
