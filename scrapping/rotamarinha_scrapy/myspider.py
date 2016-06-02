#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from keywords import ocean_keywords as keywords
from urlparse import urljoin

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
    allowed_domains = ['bbc.com']
    start_urls = [
        "http://www.bbc.com",
    ]

    def parse(self, response):
            container = response.css("div.content")
            urls = container.css("a[href*=story]::attr(href)").extract() #*= faz uma busca no css (contem)

            #coloca dominio pros links proprios do site
            for url in urls:
            	#print url
                if url[0]=='/':
                    next_url = urljoin(self.start_urls[0], url)
                else:
                    next_url = url

                yield scrapy.Request(next_url, callback=self.parse_story)

    def parse_story(self, response):

        text = u''.join(response.css('div.story-inner p::text').extract())

        #nem sempre as noticias estao nas mesmas divs...
        if not text:
            text = u''.join(response.css('div.story-body__inner p::text').extract())
            print 'ok'

        print text         
        # verificar se existem tags relevantes na notícia
        tags = []
        for keyword in keywords:
            if keyword in text:
                tags.append(keyword)

        print tags
        #só salva notícias com mais de duas tags
        story = None
        if len(tags) > 2:
            story = NewsItem()
            story['url'] = response.url
            story['headline'] = response.xpath("//title/text()").extract()
            story['body'] = text
            story['tags'] = tags

        return story
