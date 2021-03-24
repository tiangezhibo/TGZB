#   PyCharm Python TGZB
#
#   FamilyAffairsCommittee.PY
#
#   If you have any questions, please contact me
#
#   please contact me liuliuliuyadong@gmail.com
#
#   Created by LYD on 2021-03-22
#
#   Copyright © 2021 LYD. All rights reserved.
import scrapy
from scrapy.http import Request,FormRequest,HtmlResponse
from parsel import Selector
import requests
class FamilyAffairsCommitteeSpider(scrapy.Spider):
    name = 'FamilyAffairsCommittee'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']

    def start_requests(self):

        # 想一个循环处理的方法
        # i = 0
        # while True:
        #     if i==0:
        #         url = 'http://www.neac.gov.cn/seac/xxgk/tzgg/index.shtml'           # 国家名族事务委员会
        #
        #     else:
        #         url = 'http://www.neac.gov.cn/seac/xxgk/tzgg/index_%d.shtml' % i    # 国家名族事务委员会
        #     i += 1

        url = 'http://www.neac.gov.cn/seac/xxgk/tzgg/index.shtml'  # 国家名族事务委员会
        yield scrapy.Request(url=url,callback=self.parse)



    def parse(self, response, **kwargs):

        select = Selector(response.text)
        titleName = select.css('.w1 ul span a::attr(title)').getall()                   #  标题
        httpUrl = select.css('.w1 ul span a::attr(href)').getall()                     #  URL
        dataTimes = select.css('.date::text').getall()                                 # 时间


        for urls in httpUrl:
            splicingUrl = 'http://www.neac.gov.cn'+urls                                 # 拼接 URL
            yield scrapy.Request(url=splicingUrl,callback=self.detailData)

        pass

    def detailData(self, response, **kwargs):

        titleName = response.xpath('/html/body/div[2]/div[2]/div/p[2]/text()').extract_first()      # 获取标题名字
        select = Selector(response.text)
        publishTime = select.css('.p2 span::text').get()                                            # 获取时间
        excelData = select.css('.Section1').getall()                                                # 表格数据
        if excelData: # 做判断，如果为表格，单独存入TXT  不是 正常存入数据
            print('我是表格')
            content = excelData[0]
            try:
                with open('./' + titleName + '.txt', 'a+', encoding='utf-8') as f:
                    f.write(titleName)
                    f.write('\n')
                    f.write('\n')
                    f.write(publishTime)
                    f.write('\n')
                    f.write('\n')
                    f.write(content)
                    f.write('\n')
            except IOError as ex:
                print('写入目标文件错误，错误原因：'.ex)
        else:
            content = select.css('.p3 P span::text').getall()
            self.writeData(titleName=titleName, publishTime=publishTime, content=content)



    def writeData(self, titleName, publishTime, content):
        try:
            with open('./'+ titleName +'.txt','a+',encoding='utf-8') as f:
                f.write(titleName)
                f.write('\n')
                f.write('\n')
                f.write(publishTime)
                f.write('\n')
                f.write('\n')
                for a in content:
                    print('我不是表格')
                    f.write(a)
                    f.write('\n')
        except IOError as ex:
            print('写入目标文件错误，错误原因：'.ex)


