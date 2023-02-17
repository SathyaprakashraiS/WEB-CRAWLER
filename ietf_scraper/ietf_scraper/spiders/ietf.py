import scrapy
from bs4 import BeautifulSoup
import urllib


import scrapy

class DengueSpider(scrapy.Spider):
    name = 'dengue'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Dengue']

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        content = response.xpath('//div[@class="mw-parser-output"]//p//text()').getall()
        yield {
            'title': title,
            'content': ' '.join(content)
        }

