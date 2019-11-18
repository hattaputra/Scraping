# -*- coding: utf-8 -*-

# import string
import scrapy
# from scrapy import Request

class QuoteesxtractorSpider(scrapy.Spider):
    name = 'quoteExe'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    page_number = 2

    def parse(self, response):
        for quote in response.css('.quote'):
            # print(quote.getall())
            result = {
                "text": quote.css('span.text::text').get(),
                "author": quote.css('small.author::text').get(),
                "tags": quote.css('div.tags a.tag::text').getall()
            }
            yield result

        next_page = 'http://quotes.toscrape.com/page/' + str(QuoteesxtractorSpider.page_number) + '/'
        if QuoteesxtractorSpider.page_number <= 1000:
            QuoteesxtractorSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)