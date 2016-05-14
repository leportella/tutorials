#!/usr/bin/python
# -*- coding: utf-8 -*-
from keywords import ocean_keywords
from scrap_urls import FindLinks, FindArticles
import sys
import time

url = "http://www.brasil.gov.br/meio-ambiente/ultimas-noticias-meio-ambiente"
class_name = 'tileContent'
url_keyword = 'meio-ambiente'
print('Finding links...')
links = FindLinks(url,class_name,url_keyword)

keywords = ocean_keywords
ocean_links=[]
print('Finding interesting links...')
c=0
for link in links:
	textopuro = FindArticles(link)
	count=1
	valid_keywords=[]
	while count<2: #exige duas keywords para funcionar
		for keyword in keywords:
			try:
				if str(keyword) in textopuro.encode('utf-8'):
					count+=1
					valid_keywords.append(keyword)
			except UnicodeEncodeError:
				if unicode(keyword).encode('unicode_escape') in textopuro.encode('utf-8'):
					count+=1
					valid_keywords.append(keyword)
	ocean_links.append({
		'link': link,
		'keywords': valid_keywords,

	})
	c+=1
	print c
	time.sleep(1)

if len(ocean_keywords)>0: print 'ok'
else: print 'something went wrong'