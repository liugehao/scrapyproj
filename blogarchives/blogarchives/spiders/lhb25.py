from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from blogarchives.items import ArchivesItem
from scrapy.http import Request
import re
from urlparse import urljoin 

class ThinkpySpider(CrawlSpider):
    name = "lhb"
    allowed_domains = ["www.cnblogs.com"]
    download_delay = 1
    start_urls = ['http://www.cnblogs.com/lhb25/']
    #http://www.cnblogs.com/lhb25/archive/2012/10/08/45-creative-and-funny-404-error-pages.html
    rules = (
        Rule(SgmlLinkExtractor(allow=r'lhb25/archive/\d{4}/\d{2}/\d{2}/.*?\.html$'), callback='parse_item', follow=False),
        Rule(SgmlLinkExtractor(allow=r'lhb25', deny=r'ReturnUrl'), follow=True)
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = ArchivesItem()
        i['url'] = response.url
        i['title'] = hxs.select('//*[@id="cb_post_title_url"]/text()').extract()[0]
        i['content'] = hxs.select('//*[@id="cnblogs_post_body"]').extract()[0]
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
