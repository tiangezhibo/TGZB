import scrapy
import os

class FamilyaffairscommitteeOpenrecruitSpider(scrapy.Spider):
    name = 'FamilyAffairsCommittee_OpenRecruit'
    mainUrl = 'http://www.neac.gov.cn/'  # 主网站
    path = 'D:\py\TGZB\TGZB_Spiders\TGZB_Spiders\中华人民共和国国家名族事务委员会/'  # 文件夹存放位置
    def start_requests(self):
        lawsregulationUrl = self.mainUrl + 'seac/xxgk/gkzp/index.shtml'  # 主页面URL
        # lawsregulationUrl = 'http://www.neac.gov.cn/seac/xxgk/202012/1143888.shtml'
        yield scrapy.Request(url=lawsregulationUrl,callback=self.parse)


    def parse(self, response, **kwargs):
        category = response.css('.xxgkdh p span::text').get()  # 分类
        os.path.exists(self.path)
        isExists = os.path.exists(self.path + category)
        if not isExists:
            os.makedirs(self.path + category)
        else:
            print('存在')
        titleName = response.css('.w1 span a::attr(title)').getall()
        datailsUrl = response.css('.w1 span a::attr(href)').getall()
        # yield scrapy.Request(url='http://www.neac.gov.cn/seac/xxgk/202012/1143844.shtml', callback=self.detailData, meta={'path': self.path + category})
        for urls in datailsUrl:
            yield scrapy.Request(url=self.mainUrl + urls, callback=self.detailData, meta={'path': self.path + category})

    def detailData(self, response, **kwargs):
        excle = response.css('.p3 table tbody').getall()
        titleName = response.css('.f1-3-1 p.p1::text').get()
        publishTime = response.css('.f1-3-1 p.p2 span::text').getall()
        content = response.css('.f1-3-1 .p3 p span::text').getall()
        try:
            with open(response.meta['path'] + '/' + titleName + '.txt', 'a+', encoding='utf-8') as f:
                if excle:
                    f.write(response.css('.f1-3').get())
                else:
                    f.write(titleName)
                    f.write('\n')
                    f.write('\n')
                    f.write(publishTime[0])
                    f.write(publishTime[1])
                    f.write('\n')
                    for a in content:
                        f.write(a)
                        f.write('\n')
                        f.write('\n')

        except IOError as ex:
            print('写入目标文件错误，错误原因：'.ex)
