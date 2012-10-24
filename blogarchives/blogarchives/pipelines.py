# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
#import sqlite3
#from os import path
 
#from scrapy import signals
#from scrapy.xlib.pydispatch import dispatcher
#import MySQLdb
#from twisted.enterprise import adbapi
import datetime
#import MySQLdb.cursors
import psycopg2
 
class PGSQLStorePipeline(object):
    
    def __init__(self):
        self.dbconn = psycopg2.connect("dbname=scrapy user=scrapy password=mima host=localhost")
        self.db = self.dbconn.cursor()
    def process_item(self, item, spider):
        # run db query in thread pool
        if item['type'] != 'pic':
            self.db.execute('insert into itblog.archives (url,title,content) values(%(url)s , %(title)s , %(content)s )', 
                          item)
            self.dbconn.commit()
         
        return item
     
    
    def handle_error(self, e):
        pass
        #log.err(e)
        
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
import os
from blogarchives import settings
class MyImagesPipeline(ImagesPipeline):

    
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            print '-' * 100
            print urljoin_rfc(item['url'],image_url)
            yield Request(urljoin_rfc(item['url'],image_url))
            
    def item_completed(self, result, item, info):
        for ok, x in result:
            if ok:
                #image filename change  to title
                filename = os.path.join(settings.IMAGES_STORE,x['path']) 
                
                fn = os.path.basename(x['path']).split('.')
                print filename,filename.replace(fn[0],item['title'])
                os.rename(filename, filename.replace(fn[0],self.replaceBadCharOfFileName(item['title'])))
                
    def replaceBadCharOfFileName(self, fileName):
        return fileName.replace("\\","").replace("/","").replace(":","").replace("*","").replace("?","").replace("\"","").replace("<","").replace(">","").replace("|","").replace(" ","") 
        
        
    """
    def item_completed(self, results, item, info):        
        image_paths = dict([(x['url'],x['path']) for ok, x in results if ok])
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths.keys()
        for x,y in image_paths.items():
            item['content'][0] =item['content'][0].replace(x,y)
        return item
    """
"""
class MysqlStorePipeline(object):
 
    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
 
    def process_item(self,  item,domain):
        self.conn.execute('insert into cnbeta (url,name) values(%(url)s,%(name)s)', 
                          dict(url=item['url'], name=item['title']))
        #self.conn.commit()
        return item
 
    def initialize(self):
        conn = MySQLdb.Connect(host='localhost', user='root', passwd='liuyu',db='scrapy',charset='utf8')
        self.conn = conn.cursor()
        
 
    def finalize(self):
        if self.conn is not None:
            #self.conn.commit()
            self.conn.close()
            self.conn = None
 

        
class SQLiteStorePipeline(object):
    filename = 'data.sqlite'
 
    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)
 
    def process_item(self,  item,domain):
        self.conn.execute('insert into scrapy values(?,?,?)', 
                          (item['url'], item['name'], item['text']))
        self.conn.commit()
        return item
 
    def initialize(self):
        if path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
        else:
            self.conn = self.create_table(self.filename)
 
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None
 
    def create_table(self, filename):
        conn = sqlite3.connect(filename)
        conn.execute("create table scrapy
                     (url text primary key, title text, content text))
        conn.commit()
        return conn
        
class T1Pipeline(object):
    def process_item(self, item, spider):
        return item
"""
