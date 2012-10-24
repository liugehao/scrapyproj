from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import BaseSpider
from blogarchives.items import ArchivesItem
from scrapy.http import Request
import re
from scrapy.utils.url import urljoin_rfc

class QwbusSpider(BaseSpider):
    name = "qwbus"
    allowed_domains = ["qwbus.com"]
    start_urls = ['http://www.qwbus.com/photo/?page=1',
                  'http://www.qwbus.com/photo/?page=11',
                  'http://www.qwbus.com/photo/?page=19'
                  ]
    #http://www.qwbus.com/photo/?page=1

    def parse(self, response):
        hxs = HtmlXPathSelector(response)        
        titles = hxs.select('//html/body/div/div/div/div/pre/text()').extract()
        images = hxs.select('/html/body/div/div/div/div/pre/img/@src').extract()
        for url in hxs.select('//html/body/div/div/div/a/@href').extract():
            yield Request(urljoin_rfc(response.url, url), callback = self.parse)
        for i in range(len(titles)):            
            item = ArchivesItem()
            item['url'] = response.url
            item['title'] = titles[i]
            item['content'] = titles[i]
            item['image_urls'] = [images[i],]
            item['type'] = 'pic'
            yield item
"""
    
class QwbusSpider(CrawlSpider):
    name = "qwbus"
    allowed_domains = ["qwbus.com"]
    start_urls = ['http://www.qwbus.com/photo/?page=1',
                  'http://www.qwbus.com/photo/?page=11',
                  'http://www.qwbus.com/photo/?page=19'
                  ]
    #http://www.qwbus.com/photo/?page=1
    rules = (
        Rule(SgmlLinkExtractor(allow=r'photo/\?page='), callback='parse_item', follow=False),
        Rule(SgmlLinkExtractor(allow=r'photo/\?page='),  follow=True),
    )
    
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)        
        titles = hxs.select('//html/body/div/div/div/div/pre/text()').extract()
        images = hxs.select('/html/body/div/div/div/div/pre/img/@src').extract()
        for i in range(len(titles)):            
            item = ArchivesItem()
            item['url'] = response.url
            item['title'] = titles[i]
            item['content'] = titles[i]
            item['image_urls'] = [images[i],]
            item['type'] = 'pic'
            yield item   

"""
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