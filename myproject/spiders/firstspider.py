import scrapy
from lxml import etree

class FirstSpider(scrapy.Spider):
    name = 'firstspider'

    start_urls = ['http://ww.baidu.com']

    def parse(self, response):
        print(response.text)

class wbSpider(scrapy.Spider):
    name = 'wbtc'
    start_urls = ['http://bj.58.com/chuzu/?PGTID=0d100000-0000-10d1-5793-3b63d5b680a1&ClickID=1']
    def parse(self, response):
        # html = etree.HTML(response.text)
        a = response.xpath('//div[@class="des"]/h2/a//text()').extract()
        print(a)
        # for x in a:
        #     print(str(x).strip())

