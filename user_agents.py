import scrapy


class UserAgentsSpider(scrapy.Spider):
    name = 'user_agents'
    allowed_domains = ['deviceatlas.com']
    start_urls = ['https://deviceatlas.com/blog/list-of-user-agent-strings']

    def parse(self, response):
        for user_str in response.xpath('//h2/following-sibling::table/tbody/tr/td/text()[1]').extract():
            yield {
                "agent": user_str
            }
