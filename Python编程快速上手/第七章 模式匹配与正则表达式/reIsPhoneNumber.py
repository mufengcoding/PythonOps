import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = phoneNumRegex.search('My number is 999-333-4444')

print(mo)

print('Number is found:' + mo.group())

# 测试正则的在线工具 http://regexpal.com/

print(mo.group(2))
# goup不传参数返回所有

# 返回所有的分组
print(mo.groups())
area, mainNumber = mo.groups()
print(area)
print(mainNumber)

batRegex = re.compile(r'car(ar)?t')
mo1 = batRegex.search("cart is carrrdqwd csddfwe carart")
print(mo1)

batRegex = re.compile(r'car(ar)*t')
mo2 = batRegex.search(" is carrrdqwd csddfwe carart")
print(mo2)
