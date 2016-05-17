import scrapy
from keywords import ocean_keywords as keywords

#scrapy runspider top_asked_so_questions.py -t json -o results.json

class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    headline = scrapy.Field()
    body = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()


class BBCSpider(scrapy.Spider):
    name = 'bbcnews'
    allowed_domains = ['bbc.co.uk']
    start_urls = [
        "http://www.bbc.co.uk/",
    ]

    def parse(self, response):
        for submission in response.css("div.main"):
            next_url = submission.css("a.title ::attr(href").extract()
            yield scrapy.Request(next_url, callback=self.parse_story)

    def parse_story(self,response):

        text = ''.join(response.css('div.story-inner p::text').extract())

        if not text:
            text = ''.join(response.css('div.story-body__inner p::text').extract())
            print 'ok'

        tags = []
        for keyword in keywords:
            try: 
                if keyword in text:
                    tags.append(keyword)
            except:
                if str(keyword) in text:
                    tags.append(keyword) 


        if len(tags) > 2:            
            story = NewsItem()
            story['url'] = response.url
            story['headline'] = response.xpath("//title/text()").extract()
            story['body'] = text
            story['tags'] = tags

        return story
