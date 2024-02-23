import time
import scrapy


from fupin.utils import create_chrome_driver

from fupin.items import FupinItem

class GysSpider(scrapy.Spider):
    name = 'gys'
    allowed_domains = ['www.fupin832.com']
    start_urls = ['https://www.fupin832.com/pages/mapSearch']

    def parse(self, response):
        selectors = response.xpath('//div[@class="main_box6_right"]/div')
        print(len(selectors))
        for selector in selectors:
            item = FupinItem()
            item['gys_name'] = selector.xpath('./div[@class="serve"]/span/text()').extract_first()
            area = selector.xpath('./div/span/div/text()').extract_first()
            item['gys_province'] = area.split('省')[0]
            item['gys_city'] = (area.split('省')[1].split('市')[0] + "市") if '市' in area else (area.split('省')[1].split('自治州')[0] + "自治州")
            item['gys_county'] = area.split('市')[1] if '市' in area else area.split('自治州')[1]

            yield item
        
        # 1. Scrapy默认回自动过滤掉重复的请求，以避免无限循环爬取同一个url。这是通过在请求中使用Request指纹
        #    来实现的。默认情况下，Request指纹由url，请求方法（GET,POST等）和请求体组成。如果两个请求的指纹相同，
        #    那么Scrapy会认为它们是同一个请求，只会处理其中一个请求，而忽略其他的重复请求。
        #    如果你想强制Scrapy重新爬取同一个url，可以在Request中设置dont_filter属性为True。
        # 2. 如果需要翻页，在这里yield一个新的Request。
        #    这里由于请求的url即使翻页也不会变，所以Request里我加了一个flag，如果flags[0]为"next"就点击下一页继续爬
        yield scrapy.Request(url=f'https://www.fupin832.com/pages/mapSearch', callback=self.parse, flags=["next"], dont_filter=True)
