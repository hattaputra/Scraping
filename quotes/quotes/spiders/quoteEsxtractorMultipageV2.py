# -*- coding: utf-8 -*-

# import string
import scrapy
import sys
# from scrapy import Request

class QuoteesxtractorSpider(scrapy.Spider):
    name = 'quoteExeV2'
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

        next = response.xpath("//nav//ul//li//a/text()").extract()
        print(next[0])
        next_page = 'http://quotes.toscrape.com/page/' + str(QuoteesxtractorSpider.page_number) + '/'
        if str(next[0]).replace(" ", "") == "Next" :
            QuoteesxtractorSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        elif str(next[1]).replace(" ", "") == "Next" :
            QuoteesxtractorSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        else:
            sys.exit(0)