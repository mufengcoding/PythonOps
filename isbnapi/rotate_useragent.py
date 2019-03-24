# -*- coding: utf-8 -*-
import random

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class EbaySpiderMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent):
        self.user_agent = user_agent

    # 从setting.py中引入设置文件
    @classmethod
    def from_crawler(cls, crawler):
        return cls(user_agent=crawler.settings.get('MY_USER_AGENT'))

    # 设置User-Agent
    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = agent
        print(u'当前User-Agent:', request.headers['User-Agent'])
