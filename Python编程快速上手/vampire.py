name = input()
age = int(input())
if name == "Alice":
    print("Hi,Alice.")
elif age < 12:
    print("你太小了！")
elif age > 200:
    print("你是魔鬼吧！")
elif age > 20:
    print("你还是个正常人")
