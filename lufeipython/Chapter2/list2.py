
lists = [2, 3, 4, 5, 2, 2, 2, 2, 6, 'vfvdf', '222']
# count =0
# for i in lists:
#     print(i,count)
#     count+=1

#enumerate枚举  结果是个对象
#
# for i,num in enumerate(lists):
#     if i % 2 == 0:
#       lists[i] = -1
# print(lists)


# 获取第二个2
count=[]
for i,num in enumerate(lists):
    if lists[i] == 2:
        count.append(i)
print(count[1])

# 通过切片获取第二个2的索引
#print(lists.index(2))
first = lists.index(2)
second = lists[lists.index(2)+1:].index(2)
print(first+second+1)