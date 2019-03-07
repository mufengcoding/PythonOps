while True:
    print("who are you?")
    name = input()
    if name != 'Joe':
        continue
    print('Hello,Joe. What is your password?(it is a fish)')
    password = input()
    if password == 'swordfish':
        break
print("闯关成功")

# 第二个if判断不成功的时候 不会走到break 所以会走到第一行
