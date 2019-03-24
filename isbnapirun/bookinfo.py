# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    book_name = scrapy.Field()  # 图书名
    book_star = scrapy.Field()  # 图书评分
    book_pl = scrapy.Field()  # 图书评论数
    book_author = scrapy.Field()  # 图书作者
    book_publish = scrapy.Field()  # 出版社
    book_date = scrapy.Field()  # 出版日期
    book_price = scrapy.Field()  # 图书价格
    # book_isbn10 = scrapy.Field()
    # book_isbn13 = scrapy.Field()
    # book_origin_title = scrapy.Field()
    # book_alt_title = scrapy.Field()
    # book_subtitle = scrapy.Field()
    # book_image = scrapy.Field()
    # book_translator = scrapy.Field() #翻译
    # book_tags = scrapy.Field() #标签
    # book_binding = scrapy.Field() #平装
    # book_series = scrapy.Field()
    # book_pages = scrapy.Field() #页数
    # book_author_intro = scrapy.Field()#简介
    # book_catalog = scrapy.Field()
