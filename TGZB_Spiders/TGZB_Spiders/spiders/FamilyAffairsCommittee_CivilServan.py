import scrapy
import os
from scrapy.http import Request,FormRequest,HtmlResponse
from parsel import Selector
import time
import requests
import re
from datetime import datetime

class FamilyaffairscommitteeCivilservanSpider(scrapy.Spider):
    name = 'FamilyAffairsCommittee_CivilServan'
    mainUrl = 'http://www.neac.gov.cn/'                     # 主网站
    path = 'D:\py\TGZB\TGZB_Spiders\TGZB_Spiders\中华人民共和国国家名族事务委员会/'  #文件夹存放位置
    bracketsRegular = re.compile(r"[[](.*?)[]]", re.S)  # 最小匹配 提取[] 内的数据
    yearTime = time.strptime('2016-01-01', "%Y-%m-%d")      # 写入2016年1月1日时间
    yearTimeStamp = time.mktime(yearTime)                   # 把2016年时间转为时间戳 下面进行时间戳判断
    def start_requests(self):

        lawsregulationUrl = self.mainUrl + 'seac/xxgk/gwykl/index.shtml'  # 主页面URL
        yield scrapy.Request(url=lawsregulationUrl, callback=self.parse)  # 传入下一个方法





        # heads = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        # }
        # i = 1 # 从 1开始  因为页面 是1开始的
        # j = 0 # J是为了 while循环，当时间小于2016年的时间 j+1 然后结束while 循环
        # while True:
        #     if j <= 0:# j小于等于0 则循环 否则 结束循环
        #         if i == 1:
        #             lawsregulationUrl = self.mainUrl + 'seac/xxgk/gwykl/index.shtml'                # 主页面URL
        #         else:
        #             lawsregulationUrl = self.mainUrl + 'seac/xxgk/gwykl/index_%d.shtml' % i         # page + num 页面URL
        #         req = requests.get(url=lawsregulationUrl, headers=heads)
        #         select = Selector(req.text)
        #         dates = select.css('.w1 span.date::text').getall()  #  获取发布时间
        #         for a in dates:
        #             datex = re.findall(self.bracketsRegular, a)[0]
        #             tiems = time.strptime(datex, "%Y-%m-%d")                                        # 把字符串时间 转为系统时间
        #             timestamp = time.mktime(tiems)                                                  # 把系统时间 转为时间戳
        #             if int(timestamp) > int(self.yearTimeStamp):                                    # 时间戳大小判断
        #                 print('时间大于2016年')
        #
        #                 yield scrapy.Request(url=lawsregulationUrl, callback=self.parse)            # 传入下一个方法
        #                 i += 1  # 每次+1page
        #                 # time.sleep(0.5)  # 睡0.1秒
        #             else:
        #                 print('时间小于2016年，结束遍历 ')
        #                 j += 1
        #                 break
        #     else:
        #         break





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
        releaseTime = response.css('.w1 span.date::text').get()

        yield scrapy.Request(url='http://www.neac.gov.cn/seac/xxgk/202010/1142939.shtml', callback=self.detailData, meta={'path': self.path + category})

        # for urls in datailsUrl:
        #     yield scrapy.Request(url=self.mainUrl+urls,callback=self.detailData,meta={'path':self.path+category})

    def detailData(self,response, **kwargs):
        excle = response.css('.Section1 table tbody').getall()
        titleName = response.css('.f1-3-1 p.p1::text').get()
        publishTime = response.css('.f1-3-1 p.p2 span::text').getall()
        content = response.css('.p3 p').getall()
        bracketsRegular = re.compile(r'<strong>(.*?)</strong>', re.S)
        bracketsRegular1 = re.compile(r'<span(.*?)>(.*?)</span>', re.S)
        for a in content:
            print(a)
            # print(re.findall(bracketsRegular,a))
            # if len(re.findall(bracketsRegular1,a)) == 0:
            #     print('没有数据')
            # else:
            #     print(re.findall(bracketsRegular1, a))



        # for a in content:
        #     if u'\u4e00' <= a <= u'\u9fff' or u'\u0030' <= a <= u'\u0039':
        #         print('我是中文或者数字')
        #     else:
        #         print('我不是中文')







        # content1 = response.css('.p3 p span::text').getall()
        # print(content1)
        # i = 0
        # try:
        #     with open(response.meta['path'] + '/' + titleName + '.txt', 'a+', encoding='utf-8') as f:
        #         if excle:
        #             f.write(response.css('.f1-3').get())
        #         else:
        #             f.write(titleName)
        #             f.write('\n')
        #             f.write('\n')
        #             f.write(publishTime[0])
        #             f.write(publishTime[1])
        #             f.write('\n')
        #             for a in content:
        #                 f.write(a)
        #                 f.write('\n')
        #                 f.write(content1[i])
        #                 f.write('\n')
        #                 f.write('\n')
        #                 i+=1
        #
        # except IOError as ex:
        #     print('写入目标文件错误，错误原因：'.ex)
