# -*- coding: utf-8 -*-
import scrapy


class QuoteesxtractorSpider(scrapy.Spider):
    name = 'quoteEsxtractor'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('.quote') :
            # print(quote.getall())
            result = {
                "text": quote.css('span.text::text').get(),
                "author": quote.css('small.author::text').get(),
                "tags": quote.css('div.tags a.tag::text').getall()
            }
            yield result