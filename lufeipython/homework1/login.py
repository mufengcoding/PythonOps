count = 0
with open('./userlist', 'r+') as f:
    lines = f.readlines()

    def auth(count):
        username = input("输入用户名：")
        password = input("输入密码：")
        for num,line in enumerate(lines):
            line = line.split(',')
            if username == line[0]:
                if password == line[1]:
                    print("Login success!")
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


