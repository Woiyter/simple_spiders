import scrapy


class NotebooksSpider(scrapy.Spider):
    name = 'notebooks'
    allowed_domains = ['rozetka.com.ua']
    start_urls = ['https://rozetka.com.ua/']
    page_count = 67

    def start_requests(self):
        for page in range(1, 1+self.page_count):
            url = f'https://rozetka.com.ua/notebooks/c80004/page={page}'
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response, **kwargs):
        for href in response.css('a.goods-tile__picture::attr(href)').extract():
            yield scrapy.Request(href, callback=self.parse)

    def parse(self, response, **kwargs):
        characteristics = response.css('.characteristics-simple__sub-list > li > a::text').extract()
        item = {
            "Price": response.css('.product-prices__big::text').get(),
            "Title": response.css('.product__title::text').get(),
            "Diagonal": characteristics[0],
            "Resolution": characteristics[1],
            "OS": characteristics[2]
        }
        yield item
