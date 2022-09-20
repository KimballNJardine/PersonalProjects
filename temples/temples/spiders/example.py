import scrapy


class ConstructionSpider(scrapy.Spider):
    name = 'construction'
    allowed_domains = ['churchofjesuschristtemples.org']
    start_urls = ['http://churchofjesuschristtemples.org/status/']

    def parse(self, response):
        pass
