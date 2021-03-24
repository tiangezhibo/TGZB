import scrapy


class CountrySpidersSpider(scrapy.Spider):
    name = 'Country_spiders'
    def start_requests(self):
        url = 'https://www.miit.gov.cn/search/wjfb.html?websiteid=110000000000000'               #



    def parse(self, response):
        pass
