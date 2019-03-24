import json

import bs4
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/api', methods=['get'])
def get_bookinfo():
    isbn = request.args.get("isbn")
    url = "http://www.bookschina.com/book_find2/?stp=" + isbn + "&sCate=2"
    r = requests.get(url)
    content = bs4.BeautifulSoup(r.content, "lxml")
    test = content.select('.listLeft > .bookList')
    print(test)
    name = test[0].find_all(name='h2', attrs={"class": "name"})[0].get_text()
    image = test[0].find_all(name='img', attrs={"class": "lazyImg"})[0].attrs['data-original']
    author = test[0].find_all(name='a', attrs={"class": "author"})[0].get_text()
    publisher = test[0].find_all(name='a', attrs={"class": "publisher"})[0].get_text()
    pulishTiem = test[0].find_all(name='span', attrs={"class": "pulishTiem"})[0].get_text()
    recoLagu = test[0].find_all(name='p', attrs={"class": "recoLagu"})[0].get_text()
    json_list = []
    json_dict = {}
    json_dict["name"] = name
    json_dict["image"] = image
    json_dict["author"] = author
    json_dict["publisher"] = publisher
    json_dict["pulishTiem"] = pulishTiem
    json_dict["recoLagu"] = recoLagu
    json_list.append(json_dict)
    ret1 = json.dumps(json_list, ensure_ascii=False, indent=4)
    return ret1.encode('utf-8').decode('utf-8')


@app.route('/apiv2', methods=['get'])
def get_bookinfo2():
    import requests
    from bs4 import BeautifulSoup

    url = 'https://book.douban.com/tag/?view=type'
    tag_dict = {}

    def get_dict():  # 接口，提供这个标签字典
        return tag_dict

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    title = soup.select('div div a h2')  # 第一步找到h2标签，因为更细致，a标签就找不到
    tag_class = []
    # 然后通过h2标签找到爷爷级标签，就是div盒子了
    for i in title:
        a = i.find_parent()  # 找到父亲a标签
        div = a.find_parent()  # 找到父亲div
        tag_title = a.select('h2')[0].get_text()[:2]  # 找到h2标签取出内容并切片取出前两个字
        tags = div.select('tr td a')  # 找到td中的a标签
        tag_list = []

        for j in tags:
            tag_list.append(j.get_text())  # 循环取出a标签中的内容
            tag_class.append(j.get_text())
        tag_dict[tag_title] = tag_list

    # for i in tag_dict:
    #     print(i + ':', end='')
    # print(tag_dict[i])
    print(tag_class)


app.run(host='0.0.0.0', port=8802, debug=True)
