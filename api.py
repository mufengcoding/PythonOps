import bs4
import os
import requests
import urllib

from isbnapi.spiders.bookspider import BookspiderSpider


def newparse():
    print('此分类结束')
    url = 'https://book.douban.com/tag/?view=type'
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
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
        # tag_dict[tag_title] = tag_list
    # start_urls = ['https://book.douban.com/tag/' + urllib.parse.quote(tag_class[0])]
    for i in range(0, len(tag_class)):
        BookspiderSpider.start_urls = ['https://book.douban.com/tag/' + urllib.parse.quote(tag_class[i])]
        os.system('scrapy crawl bookspider -o items.json')


newparse()
