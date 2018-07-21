goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 40},
        {"name": "保温杯", "price": 250},
        {"name": "小米手机", "price": 998},
        {"name": "iPhone 4s", "price": 1800},
        {"name": "奶茶", "price": 18},
        {"name": "订书机", "price": 67},
    ]

usr_name = input('请输入用户名:')
usr_pwd = input('请输入密码:')
# with open('users', encoding='utf-8') as f:                  # 验证密码
#         lis = f.readline().split(',')
#         if usr_name in lis and usr_pwd in lis:
#             print('登陆成功'.center(30, '-'))
#             while True:                                     # 打印商品
print('商品列表'.center(30, '-'))

for num, i in enumerate(goods):
    # info = '''
    # %d  %s              $%d
    # ''' % (num, i["name"], i["price"])
    # print(info)
    # print('{0:10} ==> {1:10d}'.format(i["name"], i["price"]))
    #print( "%-8s %-8s %-8f" % (num, i["name"], i["price"]))
    # # print("{0:^6}\t{1:{3}^10}\t{2:^26}".format(num, i["name"], i["price"], chr(12288)))
    # info ='''
    #  %d    %s    %f
    # '''% (num, i["name"], i["price"])
    # print('{0:^10}\t{1:^}\t{2:>20}\t'.format(num, i["name"], i["price"], chr(12288))) # 居中对齐
    # print('|%10s' %i["name"], i["price"])
    print(num,'[{name:<{len}}\t'.format(name= i["name"] + ']',  len=23 - len( i["name"].encode('GBK')) + len(i["name"])), i["price"])

# print(goods)
salary = input('请汇入预算金额:')
while True:
    shop_car = []
    usr_choice = int(input('请选择商品序号:'))
    shop_car.append(goods[usr_choice])
    if salary >= int(goods[usr_choice]['price']):
        salary -= int(goods[usr_choice]['price'])
        print('加入购物车成功'.center(20, '*'))
        print('当前余额：%d'%(salary).center(20, '*'))
        # else:
        #     print('账号或密码错误'.center(30, '-'))





