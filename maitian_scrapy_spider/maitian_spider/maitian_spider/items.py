# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class MaitianSpiderItem(scrapy.Item):
    title = Field()
    url = Field()
    price = Field()
    unit_pay = Field()
    first_pay = Field()
    month_pay = Field()
    area = Field()  # 面积
    house_type = Field()  # 户型
    orientation = Field()  # 朝向
    floor_num = Field()  # 楼层
    region = Field()  # 地区
    business_area = Field()  # 商圈
    # house_meta = Field()  # 房评价


