# -*- coding: utf-8 -*-

# Scrapy settings for mySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mySpider'

SPIDER_MODULES = ['mySpider.spiders']
NEWSPIDER_MODULE = 'mySpider.spiders'
DOWNLOAD_TIMEOUT = 360

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mySpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   'cookies':
#       {'list_mode':'h',
#             'theme':'auto',
#             'locale':'zh',
#             '_rucaptcha_session_id':'81cc41d114f7c80d679d9f74fd5f515c',
#             'over18':'1',
#             '_ym_uid':'1699936750334282433',
#             '_ym_d':'1699936750',
#             '_ym_isad':'1',
#             'cf_clearance':'D2.mWdQvXU6966HKBVLqMZaHltN4J1xhx9fRFP_vUlg-1699941639-0-1-d327fe3.22004eb6.c1ac0296-0.2.1699941639',
#             'redirect_to':'%2Frankings%2Ftop',
#             'remember_me_token':'eyJfcmFpbHMiOnsibWVzc2FnZSI6IkltaFFWR1kyZVZWNWRtbzRVR1I2WVhwNFVHMTNJZz09IiwiZXhwIjoiMjAyMy0xMS0yMVQwNjowMjozMS4wMDBaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX21lX3Rva2VuIn19--2c490aecd9055696af9271bfd65b6d566ba94c41',
#             '_jdb_session':'ZOMHIWwY7MdgGeZkN7g1rPMOgqURCukvppggPrpEQFNaKuhLWnmu8vih9O9sxOF3I8C%2BLnxu9Mv6gb%2BP%2BjopOoysgnIRuM4PS7MiGzeX6%2FtGoVHcawWjxviRfk86ndafYuyweDB3TllsBqLN7MXiKw%2BXMLKbQWFR3ntTfbQPkbQAI9Z5HvEUJcbV5yRcKIxCG%2B%2F8ac1Rs%2BqOGRLGvZI0kM4rrONltfC3C4aKPEwUX2tLt1jdf0wmFzRiGOkKg82qKZgHMDW2mjPdEl%2FuXzaShjFNClziyGHS8QOzQGdu9eIadM%2FrHQEiG%2FUFGUQ60hgjeb1sf0eim6OEdoKrNj%2FcOuHM52xgl6EjMJnVLO%2F9gxguJZDP7wiezPFJEFh9xlev33zbfp%2BPgoOr2rJSHIjaoYtRQK7d%2Bl4gCaUWqIog08oxb1QdPI%2BllWW2McaNTqb%2FH31M%2FoDWLpPkokkhZZxaBHvP--FApTCM9eZ8u8fzbO--OOmMIP3UEABqvmJQ4FPaWQ%3D%3D'
#         }
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'mySpider.pipelines.MyspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
