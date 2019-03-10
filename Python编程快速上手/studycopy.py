# copy.copy()
import copy

spam = ["A", "B", "c", "d"]
cheese = copy.copy(spam)
cheese[1] = 2
print(cheese)
print(spam)
print('----' * 3)

spam = ["A", [222, 3, 4, 5], "c", "d"]
cheese = copy.copy(spam)
cheese[1][2] = 2
print(cheese)
print(spam)
print('----' * 3)

spam = ["A", [222, 3, 4, 5], "c", "d"]
cheese = copy.copy(spam)
cheese[1] = 2
print(cheese)
print(spam)
print('----' * 3)

spam = ["A", [222, 3, 4, 5], "c", "d"]
cheese = copy.deepcopy(spam)
cheese[1][2] = 2
print(cheese)
print(spam)

# 深拷贝和前拷贝，涉及到引用，应用是会修改列表的 深拷贝列表里面的列表也会这样
