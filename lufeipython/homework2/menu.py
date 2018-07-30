# ⌚#️
# 20180728
# mufengs
# mufeng5619@gmail.com
# 三级菜单实现

# 菜单对象
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{'盱眙'}
}


flag = 'true'   #循环标识

history = []    #用户操作记录

#格式化首次输出
print("------------|一级菜单|------------".center(50))
for i, num in enumerate(menu):
    print("%s      %s".center(50) % (i, num))
    # 将menu赋给用户操作记录history
    history.append(menu)
print("-----------返回:b/back------退出:q/quit-----------".center(50))
print("注：用户输入对应的中文，如：北京")

while flag:
    option = input("用户输入：")
    #首先判断用户输入是否在列表当中
    if option in history[-1]:
        # 判断用户输入所在的那一级菜单，是否长度不为空，如果不在则赋予一个空对象
        if len(history[-1][option]) >0:
            # 遍历初history最后一个列表的内容
            for step in history[-1][option]:
                    print(step)
            menu = history[-1][option]
        else:
            print('{}')
            menu = "{}"
        # 将用户操作添加进历史列表
        history.append(menu)
    #判断用户输入的合法性

    #返回，剔除上一次的操作记录,并遍历出来
    elif option == "back" or option == "b":
        #修改判断是否处理历史记录的最外层
        if len(history) >1 :
            history.pop()
        else:
            print("已经处于最外层")

        for step in history[-1]:
            print(step)
    #退出
    elif option == "quit" or option == "q":
        exit("退出操作")
    else:
        print("用户输出不合法！")
