import scrapy
from isbnapi.bookinfo import BooksItem
from scrapy.selector import Selector


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"

    allowed_domains = ["book.douban.com"]
    start_urls = ['https://book.douban.com/tag/%E5%8E%86%E5%8F%B2']


def parse(self, response):
    sel = Selector(response)

    book_list = sel.css('#subject_list > ul > li')
    for book in book_list:
        item = BooksItem()
        try:
            # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
            item['book_name'] = book.xpath('div[@class="info"]/h2/a/text()').extract()[0].strip()
            item['book_star'] = \
                book.xpath("div[@class='info']/div[2]/span[@class='rating_nums']/text()").extract()[0].strip()
            item['book_pl'] = book.xpath("div[@class='info']/div[2]/span[@class='pl']/text()").extract()[
                0].strip()
            pub = book.xpath('div[@class="info"]/div[@class="pub"]/text()').extract()[0].strip().split('/')
            item['book_price'] = pub.pop()
            item['book_date'] = pub.pop()
            item['book_publish'] = pub.pop()
            item['book_author'] = '/'.join(pub)
            yield item
        except:
            pass
