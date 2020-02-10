from scrapy import Spider,Request
from saks.items import SaksItem
import re

class SaksSpider(Spider):
    name = 'saks_spider'
    allowed_urls = ['https://www.saksfifthavenue.com']
    start_urls = ['https://www.saksfifthavenue.com/Handbags/shop/_/N-52jzot/Ne-6lvnb5']

    def parse(self, response):
    	num_items = response.xpath('//span[@class="mainBoldBlackText totalRecords"]/text()').extract_first()
    	num_items = int(re.sub('[^\d]','',num_items))
    	# print(num_items)
    	# num_items = response.xpath('//*[@id="pc-top"]/div/span/text()').extract_first()
    	# num_items = int(re.sub('[^\d]','',num_items)) error msg: AttributeError: 'NoneType' object has no attribute 'replace'

    	# total_pages = response.xpath('//div/span[@class="mainBoldBlackText totalNumberOfPages pagination-count"]/text()').extract_first()
    	# total_pages = int(total_pages) error msg: TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'/TypeError: expected string or bytes-like object

    	total_pages = num_items//150
    	if num_items % 150 != 0:
    		total_pages +=1
    	# page_urls = [f'https://www.saksfifthavenue.com/Handbags/shop/_/N-52jzot/Ne-6lvnb5?Nao={i*150}' for i in range(30)]
    	# for i,url in enumerate(page_urls[:3]):

    	page_urls = [f'https://www.saksfifthavenue.com/Handbags/shop/_/N-52jzot/Ne-6lvnb5?Nao={i*150}' for i in range(total_pages)]
    	for i,url in enumerate(page_urls):
  
  
    		yield Request(url=url, callback=self.parse_results_page)

    def parse_results_page(self, response):
    	# print('='*55)
    	# print('we got to the next function')
    	product_urls = response.xpath('//div[@class="product-text"]/a/@href').extract()
    	# print (type(product_urls))
    	product_titles = response.xpath('//div[@class="product-text"]/a/p/span[@class="product-designer-name"]/text()').extract()
    	# print(product_titles)
    	zipped_combine = list(zip(product_urls,product_titles))
    	# print(zipped_combine)
    	for url, title in zipped_combine:
    		meta = {}
    		meta['title'] = title
    		yield Request(url=url, callback=self.parse_product_page, meta=meta)

    def parse_product_page(self,response):
    	meta = response.meta
    	# print('='*55)
    	# print(response.url)
    	# print(meta['title'])
    	final_url = response.url
    	sub_title = response.xpath('//h1[@class="product-overview__short-description"]/text()').extract_first()
    	color = response.xpath('//dd[@class="product-variant-attribute-label__selected-value"]/text()').extract_first()
    	price = response.xpath('//dd[@id="salePrice"]/span[3]/text()').extract_first()
    	price = float(re.sub(',','',price))
    	desc = response.xpath('//section[@class="product-description"]/div/text()').extract_first()
    	desc_details = response.xpath('//section[@class="product-description"]/div/ul/li/text()').extract()
    	style_id = int(response.xpath('//div[@class="product-description__product-code"]/p/text()').extract()[2])
    	product_titles = meta['title']

    	item = SaksItem()
    	item['product_titles'] = product_titles
    	item['sub_title'] = sub_title
    	item['color'] = color
    	item['price'] = price
    	item['desc'] = desc
    	item['desc_details'] = desc_details
    	item['style_id'] = style_id

    	yield item





    	