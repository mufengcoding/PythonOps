import json

import pymysql


# 读取review数据，并写入数据库
# 导入数据库成功，总共4736897条记录
def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)  # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS review")  # 习惯性
    sql = """CREATE TABLE review (
             review_id  VARCHAR(100),
             user_id  VARCHAR(100),
             business_id VARCHAR(200),
             stars INT,
             text VARCHAR(10000) NOT NULL,
             useful INT,
             funny INT,
             cool INT)"""
    cursor.execute(sql)  # 根据需要创建一个表格


def reviewdata_insert(db):
    with open('E:/data/yelp_data/dataset/review.json', encoding='utf-8') as f:
        i = 0
        while True:
            i += 1
            print(u'正在载入第%s行......' % i)
            try:
                lines = f.readline()  # 使用逐行读取的方法
                review_text = json.loads(lines)  # 解析每一行数据
                result = []
                result.append((review_text['review_id'], review_text['user_id'],
                               review_text['business_id'], review_text['stars'],
                               review_text['text'], review_text['useful'],
                               review_text['funny'], review_text['cool']))
                print(result)

                inesrt_re = "insert into review(review_id, user_id, business_id, stars, text, useful,            funny, cool) values (%s, %s, %s, %s,%s, %s,%s, %s)"
                cursor = db.cursor()
                cursor.executemany(inesrt_re, result)
                db.commit()
            except Exception as e:
                db.rollback()
                print(str(e))
                break


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用
    db = pymysql.connect("localhost", "root", "password（你的密码）", "数据库名称", charset='utf8')
    cursor = db.cursor()
    prem(db)
    reviewdata_insert(db)
    cursor.close()
