# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
#itblog.archives
class ArchivesItem(Item):
    title = Field()
    content = Field()
    url = Field()

