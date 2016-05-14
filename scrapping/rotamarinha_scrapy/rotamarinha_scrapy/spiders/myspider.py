from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items


class BBCSpider(CrawlSpider):
    name = 'bbcnews'
    allowed_domains = ['bbc.co.uk']
    start_urls = [
        "http://www.bbc.co.uk/news",
    ]

    rules = [Rule(LinkExtractor(allow=['/news/']),'parse_story')]

    def parse_story(self,response):
        story = items.NewsItem()
        story['url'] = response.url
        story['headline'] = response.xpath("//title/text()").extract()

        #nao esta coletando as informacoes de texto....
        text=[]
        for p in response.css('.story-body__inner div p::text').extract():
            text.append(p)
        story['intro']=text
        return story
