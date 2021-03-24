import requests
from parsel import Selector
import re


def llllll():
    bracketsRegular = re.compile(r'<strong>(.*?)</strong>', re.S)
    bracketsRegular1 = re.compile(r'<span(.*?)>(.*?)</span>', re.S)

    tt = '''<p style="text-indent: 2em; font-family: 宋体; font-size: 12pt; text-align: center;"><strong>第一章</strong><strong>  </strong><strong>报考政策规定</strong><span style="font-family: 宋体; font-size: 12pt;"><p></p></span></p>
<p></p>'''

    cc = '''
    <p style="text-indent: 2em; font-family: 宋体; font-size: 12pt;"><span style="font-size: 12pt; text-indent: 2em;">一、关于报考条件</span></p>

    '''

    gg = '''
    <p style="text-indent: 2em; font-family: 宋体; font-size: 12pt;"></p>
'''
    print(len(re.findall(bracketsRegular1,gg)))




    # for i in sss:
    #     if u'\u4e00' <= i <=u'\u9fff':
    #         print('我是中文')
    #     else:
    #         print('我不是中文')


if __name__ == '__main__':
    llllll()