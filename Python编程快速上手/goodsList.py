player = {'repo': '2', 'torch': '3', 'gold coin': '4', 'dagger': '5', 'arrow': '6'}


def displayInventory(players):
    print("Inventory:")
    count = 0
    for k, v in players.items():
        print(v, ' ' + k)
        count += int(v)
    print("Total number is:", count)


# 如果使用+链接需要把count改成字符串型
print("Update .....")
# displayInventory(player)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inv, addedItems):
    count = 0
    for i in inv:
        for k, v in list(addedItems.items()):
            addedItems.setdefault(i, "0")
            v = int(v)
            if i == k:
                v += 1
                addedItems[k] = str(v)
            # count += v
    displayInventory(addedItems)
    # print("Total number is:", count)


addToInventory(dragonLoot, player)
