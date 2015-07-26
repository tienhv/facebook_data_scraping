# -*- coding: utf-8 -*-

# Scrapy settings for facebook_data_scraping project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'facebook_data_scraping'

USER_AGENT = "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"

SPIDER_MODULES = ['facebook_data_scraping.spiders']
NEWSPIDER_MODULE = 'facebook_data_scraping.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'facebook_data_scraping (+http://www.yourdomain.com)'

ITEM_PIPELINES = {'facebook_data_scraping.pipelines.FacebookImagesPipeline':10}
IMAGES_STORE = "./downloaded-photos"

# Throttling
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 3
AUTOTHROTTLE_DEBUG = True
