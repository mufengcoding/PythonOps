import bs4
import json
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


app.run(host='0.0.0.0', port=8802, debug=True)
