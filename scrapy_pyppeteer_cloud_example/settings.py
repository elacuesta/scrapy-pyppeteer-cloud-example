# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_pyppeteer_cloud_example project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import os


BOT_NAME = "scrapy_pyppeteer_cloud_example"

SPIDER_MODULES = ["scrapy_pyppeteer_cloud_example.spiders"]
NEWSPIDER_MODULE = "scrapy_pyppeteer_cloud_example.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
)

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_pyppeteer.handler.ScrapyPyppeteerDownloadHandler",
    # "https": "scrapy_pyppeteer.handler.ScrapyPyppeteerDownloadHandler",
}

FEED_EXPORT_ENCODING = "utf8"
FEED_EXPORT_INDENT = 4

CONCURRENT_REQUESTS = 32

LOG_LEVEL = "INFO"

PYPPETEER_LAUNCH_OPTIONS = {}

# when running on Docker (Scrapy Cloud)
if os.environ.get("CHROMIUM_LOCAL_PATH"):
    PYPPETEER_LAUNCH_OPTIONS["executablePath"] = os.environ["CHROMIUM_LOCAL_PATH"]
