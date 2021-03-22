import scrapy


class CountrySpidersSpider(scrapy.Spider):
    name = 'Country_spiders'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
