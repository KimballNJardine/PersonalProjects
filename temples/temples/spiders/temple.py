import scrapy


class ConstructionSpider(scrapy.Spider):
    name = 'construction'
    allowed_domains = ['churchofjesuschristtemples.org']
    start_urls = ['http://churchofjesuschristtemples.org/status/']

    def parse(self, response):
        for temple in response.css('div.desc'):
            yield {
                'date' : temple.css('a::text').get(),
                'link' : temple.css('a').attrib['href']
            }
        pass
