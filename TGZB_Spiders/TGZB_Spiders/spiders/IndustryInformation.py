import scrapy
from scrapy.http import Request,FormRequest,HtmlResponse
from parsel import Selector

class IndustryinformationSpider(scrapy.Spider):
    name = 'IndustryInformation'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    def start_requests(self):
        url = 'https://www.miit.gov.cn/search/wjfb.html?websiteid=110000000000000&pg=&p=&tpl=14&category=51&q='           # 工业和信息化部
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response, **kwargs):
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print(response.text)
        # select = Selector(response.text)
        #
        # titleName = select.css('.yyfw').get()
        # print(titleName)
        print('\n')
        print('\n')
        print('\n')
        print('\n')


        pass
