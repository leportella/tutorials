#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Create by: @leportella

Objective:
Scrapy the BBC website, find news that have at least
2 of the tags listed below and add their headline, tags
and url on a json.

To run:
$ scrapy runspider myspider.py -t json -o results.json
'''

import scrapy
from urllib.parse import urljoin

keywords = [
    'Afghanistan',
    'Africa',
    'China',
    'Europe',
    'France',
    'Japan',
    'Syria',
    'Trump',
    'US',
    'country',
    'population',
    'war',
    'personality'
]

class NewsItem(scrapy.Item):
    headline = scrapy.Field()
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

        # makes the search on the css for possible news links
        types = ['story', 'news']

        urls = []
        for type in types:
            urls += container.css(
                'a[href*={}]::attr(href)'.format(type)
            ).extract()

        # some links need to add the bbc domain
        for url in urls:
            if url[0] == '/':
                next_url = urljoin(self.start_urls[0], url)
            else:
                next_url = url

            yield scrapy.Request(next_url, callback=self.parse_story)

    def parse_story(self, response):

        # get the text body
        text = u''.join(response.css('div.story-inner p::text').extract())

        # texts are not always on the same div
        if not text:
            text = u''.join(
                response.css('div.story-body__inner p::text').extract()
            )

        # check if it can find tags on the text
        tags = []
        for keyword in keywords:
            if keyword in text:
                tags.append(keyword)

        # we define that only stores the news if there is at least
        # 2 tags on the story
        story = None
        if len(tags) > 2:
            story = NewsItem()
            story['url'] = response.url
            story['headline'] = response.xpath("//title/text()").extract()
            story['tags'] = tags

        return story
