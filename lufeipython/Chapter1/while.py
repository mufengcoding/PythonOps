#
#print 1-100
#

# orgnum = 0
#
# while orgnum < 100:
#     orgnum+=1
#     print(orgnum)

#
#print 1-100 的偶数
#

# orgnum = 2
#
# while orgnum < 100:
#     #小插曲，差点偶数的概念忘了，我去
#     if orgnum%2==0:
#         print(orgnum)
#     orgnum+=1


#
#1-100 不打印50 打印80-100的平方
#
orgnum = 1

while orgnum < 100:

    if orgnum>=60 and orgnum<=80:
        print(orgnum*orgnum)
    elif orgnum == 50:
        pass   #pass代表满足条件不操作
        print("break")
        break
    else:
        print(orgnum)
    orgnum += 1
