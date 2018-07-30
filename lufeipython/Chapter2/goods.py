

goods = [["linux", 9999], ["windows", 8888], ["unix", 7777], ["kailinux",10000]]

print("---"*2,"系统列表","---"*2)

for i,num in enumerate(goods):
    print("%s.    %s       %s"%(i,goods[i][0],goods[i][1]))