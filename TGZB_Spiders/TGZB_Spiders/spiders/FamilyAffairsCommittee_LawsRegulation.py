import scrapy
from scrapy.http import Request,FormRequest,HtmlResponse
from parsel import Selector
import os


class FamilyaffairscommitteeLawsregulationSpider(scrapy.Spider):
    name = 'FamilyAffairsCommittee_LawsRegulation'

class FamilyaffairscommitteeLawsregulationSpider(scrapy.Spider):
    name = 'FamilyAffairsCommittee_LawsRegulation'
    mainUrl = 'http://www.neac.gov.cn/'                     # 主网站
    path = 'D:\py\TGZB\TGZB_Spiders\TGZB_Spiders\中华人民共和国国家名族事务委员会/'  #文件夹存放位置
    def start_requests(self):
        lawsregulationUrl = self.mainUrl + 'seac/zcfg/flfg/index.shtml'
        yield scrapy.Request(url=lawsregulationUrl,callback=self.parse)

    def parse(self, response, **kwargs):
        category = response.css('.BreadcrumbNav p span::text').get()                  # 分类
        os.path.exists(self.path)
        isExists = os.path.exists(self.path + category)
        if not isExists:
            os.makedirs(self.path + category)
        else:
            print('存在')
        detailsUrl = response.css('.w1 ul a::attr(href)').getall()                    #URL
        titleName = response.css('.w1 ul a::text').get()                              # 标题
        releaseTime = response.css('.w1 ul span::text').getall()                      # 发布时间
        # splicingUrl = self.mainUrl + detailsUrl[0]
        # yield scrapy.Request(url=splicingUrl, callback=self.detailsData,meta={'path':self.path+category})

        for url in detailsUrl:
            splicingUrl = self.mainUrl + url
            yield scrapy.Request(url=splicingUrl,callback=self.detailsData,meta={'path':self.path+category})
        pass

    def detailsData(self, response, **kwargs):
        titleName = response.css('.f1-3-1 p.p1::text').get()
        publishTime = response.css('.f1-3-1 p.p2 span::text').getall()
        content = response.css('.f1-3-1 .p3 p::text').getall()
        try:
            with open(response.meta['path'] + '/' + titleName + '.txt', 'a+', encoding='utf-8') as f:
                f.write(titleName)
                f.write('\n')
                f.write('\n')
                f.write(publishTime[0])
                f.write(publishTime[1])
                f.write('\n')
                f.write('\n')
                for a in content:
                    f.write(a)
                    f.write('\n')
                    f.write('\n')
        except IOError as ex:
            print('写入目标文件错误，错误原因：'.ex)