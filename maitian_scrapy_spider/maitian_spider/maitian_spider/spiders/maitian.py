# -*- coding: utf-8 -*-
import json
import scrapy
from maitian_spider.items import MaitianSpiderItem


class MaitianSpider(scrapy.Spider):
    name = 'maitian'
    allowed_domains = ['maitian.cn']
    start_urls = [
        'http://bj.maitian.cn/esfall',
    ]

    # 解析不同区域列表页
    def parse(self, response):
        area_list = response.css('#disregion li')
        for room in area_list:
            area_url = room.css('a::attr("href")').extract_first()
            if area_url:
                area_url = response.urljoin(area_url)
                yield scrapy.Request(url=area_url, callback=self.parse_area)

    # 处理每个区域的信息, 提取房源url和下一页链接
    def parse_area(self, response):
        house_list = response.css('.list_title')
        for house in house_list:
            house_url = house.css('h1 a::attr("href")').extract_first()
            house_url = response.urljoin(house_url)
            yield scrapy.Request(url=house_url, callback=self.parse_room)
        next_page = response.css('#paging a:nth-last-child(2)::attr("href")').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_area)

    # 处理详情页
    def parse_room(self, response):
        result = response.xpath('.').re(r'var showHouseInfo = \(\'(.*?)\'\); \/\/')[0]
        if result:
            house_infos = json.loads(result)['houseArr'][0]
            house_item = MaitianSpiderItem()
            field_map = {
                'title': 'Title', 'price': 'PriceTotal', 'unit_pay': 'PriceSingle',
                'first_pay': 'FirstPay', 'month_pay': 'MonthlyPay', 'area': 'AreaSize', 'house_type': 'Layout',
                'orientation': 'Direction', 'floor_num': 'Floor', 'region': 'RegionName',
                'business_area': 'CycleName',
            }
            for key, value in field_map.items():
                house_item[key] = house_infos[value]
            house_item['url'] = response.url
            yield house_item







