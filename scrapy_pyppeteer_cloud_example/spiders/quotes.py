import logging

from scrapy import Spider, Request
from scrapy_pyppeteer.page import PageCoroutine


logging.getLogger("pyppeteer").setLevel(logging.INFO)
logging.getLogger("websockets").setLevel(logging.INFO)


class QuotesSpider(Spider):
    name = "quotes"

    def start_requests(self):
        yield Request(
            url="http://quotes.toscrape.com/scroll",
            meta=dict(
                pyppeteer=True,
                pyppeteer_page_coroutines=[
                    PageCoroutine("waitForSelector", "div.quote"),
                    PageCoroutine("evaluate", "window.scrollBy(0, 2000)"),
                    PageCoroutine("waitForSelector", "div.quote:nth-child(11)"),
                ],
            ),
        )

    async def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("a.tag::text").getall(),
            }
