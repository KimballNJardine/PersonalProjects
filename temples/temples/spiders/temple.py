import scrapy


class TempleSpider(scrapy.Spider):
    name = 'temple'
    allowed_domains = ['churchofjesuschristtemples.org']
    start_urls = ['http://churchofjesuschristtemples.org/status/']

    def parse(self, response):
        for temple in response.css('div.desc'):
            yield {
                'date' : temple.css('a::text').get(),
                'link' : temple.css('a').attrib['href']
            }
        pass
