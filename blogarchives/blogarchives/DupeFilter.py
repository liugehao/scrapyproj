from scrapy.utils.request import request_fingerprint
from scrapy.utils.job import job_dir
from scrapy.dupefilter import BaseDupeFilter
import bsddb
import md5

class RFPDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""

    def __init__(self, path=None):
        self.db = bsddb.btopen('RFPDupeFilter.bsddb')

    @classmethod
    def from_settings(cls, settings):
        return cls(job_dir(settings))

    def request_seen(self, request):
        fp = md5.md5(request.url).hexdigest()
        if self.db.has_key(fp):
            return True
        self.db[fp] = request.url
        

    def close(self, reason):
        self.db.close()