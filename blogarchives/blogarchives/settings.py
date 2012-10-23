# Scrapy settings for blogarchives project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'blogarchives'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['blogarchives.spiders']
NEWSPIDER_MODULE = 'blogarchives.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


#SPIDER_MIDDLEWARES = { 't1.middlewares.ignore.': 560 }
#IMAGES_STORE = '/home/l/pyproject/t1/images'
#ITEM_PIPELINES = ['blogarchives.pipelines.PGSQLStorePipeline','scrapy.contrib.pipeline.images.ImagesPipeline']
ITEM_PIPELINES = ['blogarchives.pipelines.PGSQLStorePipeline']
DUPEFILTER_CLASS = 'blogarchives.DupeFilter.RFPDupeFilter'

#DEPTH_PRIORITY = 1
#SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
#SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'