# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_pyppeteer_cloud_example project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_pyppeteer_cloud_example'

SPIDER_MODULES = ['scrapy_pyppeteer_cloud_example.spiders']
NEWSPIDER_MODULE = 'scrapy_pyppeteer_cloud_example.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'scrapy_pyppeteer_cloud_example (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_pyppeteer.handler.ScrapyPyppeteerDownloadHandler",
    # "https": "scrapy_pyppeteer.handler.ScrapyPyppeteerDownloadHandler",
}

FEED_EXPORT_ENCODING = "utf8"
FEED_EXPORT_INDENT = 4
