from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from blogarchives.items import ArchivesItem
from scrapy.http import Request
import re
from urlparse import urljoin 

class ThinkpySpider(CrawlSpider):
    name = "thinkpy"
    allowed_domains = ["thinkpy.com"]
    download_delay = 1
    start_urls = ['http://thinkpy.com/']
    #http://thinkpy.com/2012/03/15/python-mysqldb-utf-8/
    rules = (
        Rule(SgmlLinkExtractor(allow=r'\d{4}/\d{2}/\d{2}/.*?'), callback='parse_item', follow=False),
        Rule(SgmlLinkExtractor(allow=r''), follow=True)
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = ArchivesItem()
        i['url'] = response.url
        i['title'] = hxs.select('//html/body/div/div[2]/div/div/div[2]/h1/text()').extract()[0]
        i['content'] = hxs.select('/html/body/div/div[2]/div/div/div[2]/div[2]').extract()[0]
        return i
        


"""
from scrapy.spider import BaseSpider

class ThinkpySpider(BaseSpider):
    name = "thinkpy"
    allowed_domains = ["thinkpy.cn"]
    start_urls = (
        'http://www.thinkpy.cn/',
        )

    def parse(self, response):
        pass 
"""