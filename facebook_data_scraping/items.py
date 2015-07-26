# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FacebookPhoto(scrapy.Item):
    username = scrapy.Field()
    image_url = scrapy.Field()
    pass


class FacebookDataScrapingItem(scrapy.Item):
    image_url = scrapy.Field()
    pass
