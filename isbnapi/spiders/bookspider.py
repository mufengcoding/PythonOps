# -*- coding: utf-8 -*-
import requests
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector

from isbnapi.items import BooksItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["douban.com"]
    url = 'https://book.douban.com/tag/?view=type'
    tag_dict = {}

    def get_dict(self):  # 接口，提供这个标签字典
        return self.tag_dict

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
            tag_class.append('https://book.douban.com/tag/' + j.get_text())
    start_urls = tag_class

    def parse(self, response):

        sel = Selector(response)
        book_list = sel.css('#subject_list > ul > li')
        for book in book_list:
            item = BooksItem()
            try:
                # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
                item['book_name'] = book.xpath('div[@class="info"]/h2/a/text()').extract()[0].strip()
                item['book_star'] = book.xpath("div[@class='info']/div[2]/span[@class='rating_nums']/text()").extract()[
                    0].strip()
                item['book_pl'] = book.xpath("div[@class='info']/div[2]/span[@class='pl']/text()").extract()[0].strip()
                pub = book.xpath('div[@class="info"]/div[@class="pub"]/text()').extract()[0].strip().split('/')
                # print(pub,)
                item['book_price'] = pub.pop()
                item['book_date'] = pub.pop()
                item['book_publish'] = pub.pop()
                item['book_author'] = '/'.join(pub)
                item['book_image'] = book.xpath('div[@class="pic"]/a/img/@src').extract()[0].strip()
                yield item
            except:
                pass

            nextPage = sel.xpath(
                '//div[@id="subject_list"]/div[@class="paginator"]/span[@class="next"]/a/@href').extract()
            # print(nextPage)

            if len(nextPage) > 0:
                if nextPage[0].strip():
                    next_url = 'https://book.douban.com' + nextPage[0].strip()

                    yield scrapy.http.Request(next_url, callback=self.parse)

# class BookspiderSpider(scrapy.Spider):
#     name = 'ip'
#     allowed_domains = []
#
#     def start_requests(self):
#
#         url = 'http://ip.chinaz.com/getip.aspx'
#
#         for i in range(4):
#             yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
#
#     def parse(self,response):
#         print(response.text)
