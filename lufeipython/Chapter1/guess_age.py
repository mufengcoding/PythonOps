
#
#逻辑三次机会猜年龄
#
age = "25"
flags = 0
count = 0


# def dogame(flags):
#     userage = int(input("猜猜多大："))
#     if userage == age and flags >1:
#         flags-=1
#         print("congridlation ! you are right,剩余次数", flags)
#         return
#     elif userage >age and flags >1:
#         flags -= 1
#         print("try smaller,剩余次数", flags)
#         dogame(flags)
#     elif userage < age and flags >1:
#         flags -= 1
#         print("try bigger,剩余次数", flags)
#         dogame(flags)
#     else:
#         print("抱歉次数用完了")
# dogame(flags)


#
#while 判断循环
#
# while flags<4 :
#     userage = input("猜猜多大:")
#     flags+=1
#     count+=1
#     if flags==4:
#         c=input("少年你挂了，是否继续Y/N？")
#         if c=="Y":
#             flags = 0
#         else:
#             print("失败","消耗",count,"次机会通关")
#             break
#
#     else:
#         if userage == age:
#             print("congridlation ! you are right,剩余次数", 3-flags)
#             print("成功", "消耗", count, "次机会通关")
#         elif userage > age:
#             print("try smaller,剩余次数", 3-flags)
#         elif userage < age:
#             print("try bigger,剩余次数", 3-flags)
#         else:
#             print("抱歉次数用完了")


#加强版
while flags<3 :
    userage = input("猜猜多大:")

    count+=1


    if userage == age:
        print("congridlation ! you are right,剩余次数", 3-flags)
        print("成功", "消耗", count, "次机会通关")
        break
    elif userage > age:
        print("try smaller,剩余次数", 3-flags)
    elif userage < age:
        print("try bigger,剩余次数", 3-flags)
    else:
        print("抱歉次数用完了")
    flags += 1
    if flags==3:
        c=input("少年你挂了，是否继续Y/N？")
        if c=="Y" or c=="y" :
            flags = 0
        else:
            print("失败","消耗",count,"次机会通关")
            break

