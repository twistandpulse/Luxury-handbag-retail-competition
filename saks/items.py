# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SaksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_titles = scrapy.Field()
    sub_title = scrapy.Field()
    color = scrapy.Field()
    price = scrapy.Field()
    desc = scrapy.Field()
    desc_details = scrapy.Field()
    style_id = scrapy.Field()
    
