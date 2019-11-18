# -*- coding: utf-8 -*-

import string
import scrapy
from scrapy import Request

class QuoteesxtractorSpider(scrapy.Spider):
    name = 'quoteEsxtractor'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse_page(self, response):
        for quote in response.css('.quote') :
            # print(quote.getall())
            result = {
                "text": quote.css('span.text::text').get(),
                "author": quote.css('small.author::text').get(),
                "tags": quote.css('div.tags a.tag::text').getall()
            }
            yield result
        next_urls = response.xpath("//ul[@class='pager']//li[@class='next']//a/@href").extract()
        for next_url in next_urls :
            yield Request(response.urljoin(next_url), callback=self.parse_page())