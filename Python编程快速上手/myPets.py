myPets = ['tom', 'joke', 'lili']
# 输入宠物名称
print('Enter a pet name:')
name = input()
if name not in myPets:
    print(' i have no pet named :' + name)
else:
    print(name + ' is my pet')

mys = " tomca is not a cat "
Newpets = mys[0:4] + "222" + mys[5:11]
print(Newpets)
