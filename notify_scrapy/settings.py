# -*- coding: utf-8 -*-

# Scrapy settings for notify_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from datetime import datetime

BOT_NAME = 'notify_scrapy'

SPIDER_MODULES = ['notify_scrapy.spiders']
NEWSPIDER_MODULE = 'notify_scrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'notify_scrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # The websites of school doesn't have robots.txt

COMMANDS_MODULE = 'notify_scrapy.commands'

EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'notify_scrapy.middlewares.NotifyScrapySpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'notify_scrapy.middlewares.NotifyScrapyDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# The integer values assigned to classes in this setting determine the order in which they run
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'notify_scrapy.check_pipelines.ContentCheckPipeline': 0,
    'notify_scrapy.check_pipelines.ItemCheckPipeline': 10,
    'notify_scrapy.check_pipelines.DateTimeHandlerPipeline': 20,
    'notify_scrapy.check_pipelines.TimeLimitCheckPipeline': 30,
    'notify_scrapy.check_pipelines.TagsHandlerPipeline': 40,
    'notify_scrapy.db_pipelines.NoticeMYSQLPipeline': 50,
    'notify_scrapy.db_pipelines.PublisherAutoRegisterPipeline': 60,
    'notify_scrapy.html_content_pipelines.FetchHTMLContentPipeline': 100,
    'notify_scrapy.html_content_pipelines.HTMLContentCheckPipeline': 110,
    'notify_scrapy.html_content_pipelines.HTMLContentCleanerPipeline': 120,
    'notify_scrapy.html_content_pipelines.RelativeURLHandlerPipeline': 130,
    'notify_scrapy.db_pipelines.HTMLContentMYSQLPipeline': 140,
}

TIME_ZONE = 'Asia/Shanghai'

# Time limit
NOTICE_TIME_LIMIT = datetime(2022, 2, 1, 0, 0, 0, 0)

# Configure MySQL
MYSQL_URI = '127.0.0.1'       # Change it if necessary
MYSQL_USER = 'root'
MYSQL_USER_PASSWORD = '123456'
MYSQL_DATABASE = 'notify_2021'
MYSQL_COLLECTION_NAME = 'notices'
MYSQL_HTML_CONTENT_COLLECTION_NAME = 'html_content'
MYSQL_PUBLISHERS_COLLECTION_NAME = 'publishers'
MYSQL_PUBLISHER_GROUPS_COLLECTION_NAME = 'publisher_groups'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
