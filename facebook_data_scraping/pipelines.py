# -*- coding: utf-8 -*-

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
import re

class FacebookImagesPipeline(ImagesPipeline):

    CONVERTED_ORIGINAL = re.compile('^full/[0-9,a-f]+.jpg$')

    def get_media_requests(self, item, info):
        yield Request(item["image_url"], meta={'username': item["username"]})

    # this is where the image is extracted from the HTTP response
    def get_images(self, response, request, info):
        for key, image, buf, in super(FacebookImagesPipeline, self).get_images(response, request, info):
            if self.CONVERTED_ORIGINAL.match(key):
                key = self.change_filename(key, response)
                yield key, image, buf

    def change_filename(self, key, response):
        org_filename = response.url.split('/')[-1]
        org_filename = org_filename[:org_filename.find(".jpg") + 4]
        username = response.meta['username']
        new_filename = '{0}-{1}'.format(username, org_filename)
        return new_filename

class FacebookDataScrapingPipeline(object):
    def process_item(self, item, spider):
        return item
