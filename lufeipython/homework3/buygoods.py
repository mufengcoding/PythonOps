#时间：20180730
#作者：mufengs
#修改：加上对用户啊判断的检测，以及操作输出的修改

goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]


count = 0

def printlist():
    print("---" * 2, "商品列表", "---" * 2)

    for i, good in enumerate(goods):
        print("%s.    %s       %s" % (i, good["name"], good["price"]))
#
#登陆模块
#
with open('./userlist', 'r+') as f:
    lines = f.readlines()
    #定义一个auth函数
    def auth(count):
        username = input("输入用户名：")
        password = input("输入密码：")
        for num,line in enumerate(lines):
            line = line.split(',')
            #判断用户是否存在
            if username == line[0]:
                #判断密码是否正确
                if password == line[1]:
                    print("Login success!欢迎来到路飞小店")
                    #输入本人发的工资
                    pay = input("请输入本月工资：")
                    #判断输入的合法性
                    if pay == "":
                        print("输入有误，退出")
                        break
                    else:
                        pay = int(pay)

                    printlist()
                    #设置while循环标识符
                    todo = "true"
                    # 定义一个购物车
                    buygoods = []
                    while todo:
                        inputtmp = input("输入需要购买的商品编号:")
                        if inputtmp.isdigit() and int(inputtmp) <= len(goods):

                            buy = int(inputtmp)

                            # 商品的价格
                            buys = int(goods[buy]["price"])
                            # 判断商品价格是否大于工资余额
                            if goods[buy]["price"] > pay:
                                print("\033[0;31m%s\033[0m"%"你的工资不够购买该产品！")
                            else:
                                # 定义临时变量
                                tmp = {}
                                pay -= buys
                                #已买到的产品
                                buygood = goods[buy]["name"]
                                tmp["name"] = buygood
                                tmp["price"] = buys
                                tmp["pay"]= pay #余额
                                #加入购物车
                                buygoods.append(tmp)
                                print("\033[0;31m%s\033[0m"%(buygood),"已加入购物车")
                                print("\033[0;31m%s\033[0m   \033[0;31m%s\033[0m "%("工资余额：",pay))
                            # 判断是否继续购物
                            con = input("是否继续,y/Y继续，其他输入退出")
                            if con == "y" or con == "yes":
                                printlist()
                            else:
                                # 退出这边修改标识符好像while还是会循环 有点奇怪
                                todo = "false"
                                print("---" * 2, "已买到商品", "---" * 2)
                                #遍历出购物车里面的商品
                                for i in buygoods:
                                    print("---" * 2,"\033[0;31m%s\033[0m "%(i["name"]),"---" * 2)
                                print("---" * 2,"\033[0;31m%s\033[0m   \033[0;31m%s\033[0m "%("剩余工资:",buygoods[0]["pay"]), "---" * 2) #取任意一个取出剩余金额

                                exit()
                        else:
                            print("小伙子，你的输入不合法")
                            printlist()
                    break
                elif int(line[2]) >= 3:
                        print("用户被锁定")
                        break
                else:
                    flags = int(line[2])
                    flags += 1
                    line[2] = ','.join('%d'%flags)
                    line=",".join(line)+"\n"
                    lines[num]=line
                    print("密码错误！剩余机会", 3-flags,'次')
                    control = input("是否继续登陆Y/N?")
                    if control in {"Y", "y"}:

                        auth(count)
                    else:
                        print("推出系统")
            else:
                count+=1
                pass
        if count == 4:
            print("非法用户")
        # print(count)
        open('./userlist', 'w').writelines(lines)

auth(count)


