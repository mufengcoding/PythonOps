# -------------------------
# author：mufengs
# -------------------------

hometown = input("家乡:")
name = input("姓名:")
age = float(input("年龄:"))

# print("-----------info------------")
# print("--家乡：    ", hometown)
# print("--姓名：    ", name)
# print("--年龄：    ", age)

info='''-------------info of %s--------------------
Name:                %s
Age:                 %f
Hometown:            %s
-------------------end------------------------
'''%(name,name,age,hometown)
print(info)

# %s字符串
# %d数字
# %f小数
