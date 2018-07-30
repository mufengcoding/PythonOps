lists = [ 2,3,4,5,2,2,2,2,6,'vfvdf' ]
#a = lists.index(1)
a = lists[2]
b = lists.index(2)  #去除索引
c = lists[lists.index(2)]
print(c)

print("*"*72)
print("*"*30,'mufengs',"*"*33)
print("*"*72)
d = lists.count(2)
print(d)

print("-----------切片--------------")

e = lists[0:5]
print(e)

f = lists[2:-2]
print(f)

g = lists[0:5:3]  #第三个参数的含义是步长的意思
print(g)

print(lists.__len__())
print(len(lists))

lists.append("222")
print(lists)
lists.pop()
print(lists)
lists.insert(1,'33')
lists = lists[4:5]
print(lists)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])

print(L[1][1])

print(L[2][2])