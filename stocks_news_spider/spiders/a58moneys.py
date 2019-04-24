# -*- coding: utf-8 -*-
import scrapy
from stocks_news_spider.items import NewsItem

class A58moneysSpider(scrapy.Spider):
    name = '58moneys'
    allowed_domains = ['58moneys.com']
    start_urls = ['https://www.58moneys.com/finance.html']
    base_url = 'https://www.58moneys.com/'

    def parse(self, response):
        news = response.xpath('//*[@id="ajaxGetNewsList"]/ul/li')
        for each in news:
            item = NewsItem()
            item["title"] = each.xpath('./div[1]/a/text()').extract()[0]
            item["time"] = each.xpath('./div[2]/text()').extract()[0]
            item["href"] = self.base_url + each.xpath('./div[1]/a/@href').extract()[0]
            print(item)