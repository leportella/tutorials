#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from keywords import ocean_keywords as keywords

# para rodar...
# scrapy runspider top_asked_so_questions.py -t json -o results.json

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
        "http://www.bbc.co.uk",
    ]

    def parse(self, response):
            container = response.css("div.container")
            urls = container.css("a ::attr(href)").extract()

            #coloca dominio pros links proprios do site
            for url in urls:
                if url[0]=='/':
                    next_url = start_urls[0] + url
                else:
                    next_url = url

                yield scrapy.Request(next_url, callback=self.parse_story)

    def parse_story(self,response):

        text = ''.join(response.css('div.story-inner p::text').extract())

        #nem sempre as noticias estao nas mesmas divs...
        if not text:
            text = ''.join(response.css('div.story-body__inner p::text').extract())
            print 'ok'

        # verificar se existem tags relevantes na notícia
        tags = []
        for keyword in keywords:
            try: 
                if keyword in text:
                    tags.append(keyword)
            except:
                if str(keyword) in text:
                    tags.append(keyword) 

        #só salva notícias com mais de duas tags
        if len(tags) > 2:            
            story = NewsItem()
            story['url'] = response.url
            story['headline'] = response.xpath("//title/text()").extract()
            story['body'] = text
            story['tags'] = tags

        return story
