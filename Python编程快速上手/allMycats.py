# print('Enter the name of cat 1:')
# catName1 = input()
# print('Enter the name of cat 2:')
# catName2 = input()
# print('Enter the name of cat 3:')
# catName3 = input()
# print('Enter the name of cat 4:')
# catName4 = input()
# print('Enter the name of cat 5:')
# catName5 = input()
# print("The cat names are:")
# print(catName1+' '+catName2+' '+catName3+' '+catName4+' '+catName5)


cat = []
while True:
    print('Enter the name of cat ' + str(len(cat) + 1) + ' (Or Enter nonthing to stop.)')
    name = input()
    if name == '':
        break
    cat = cat + [name]
print("The cat names are:", end=' ')
for i in cat:
    print((' ' + i), end=' ')
