import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse

from ..items import BeikeItem

class ZufangSpider(scrapy.Spider):
    name = "zufang"
    allowed_domains = ["bj.zu.ke.com"]
    
    def start_requests(self):
        total = 1145
        limit = 30
        for i in range(0,total//limit + 1):
            url = f'https://bj.zu.ke.com/zufang/shuangjing/pg{i+1}/#contentList'
            
            yield Request(url)

    def parse(self, response:HtmlResponse):
        item = BeikeItem()

        blocks = response.css('.content__list--item')
        for it in blocks:
            item['title'] = it.css('.content__list--item--title a.twoline::text').get().strip()
            item['rent'] = it.css('.content__list--item-price em::text').get()
            
            bls = it.css('.content__list--item--des a[target="_blank"]')
            temp = []
            for b in bls:
                temp.append(b.css('::text').get())
            item['addr'] = temp

            bls = it.css('.content__list--item--des::text').getall()
            temp = []
            for b in bls:
                temp.append(b.strip())
            item['info'] = temp

            bls = it.css('.content__list--item--bottom i')
            temp = []
            for b in bls:
                temp.append(b.css('::text').get())
            item['remark'] = temp

            item['supplier'] = it.css('.content__list--item--brand .brand::text').get().strip()

            yield item
