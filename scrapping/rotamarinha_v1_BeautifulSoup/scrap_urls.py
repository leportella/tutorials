#!/usr/bin/python
# -*- coding: utf-8 -*-

#For Python 2.7

import urllib2
from BeautifulSoup import BeautifulSoup


def FindLinks(url,class_name,url_keyword=None):
    url = url
    text = urllib2.urlopen(url).read()
    soup = BeautifulSoup(text)
    data = soup.findAll('div',attrs={'class':class_name})

    links=[]
    for div in data:
        Tag_a = div.findAll('a')
        for a in Tag_a:
            temp = a['href'].split('/')
            if url_keyword:
                for i in temp:
                    if i==url_keyword:
                        links.append(a['href'])
            else:
                links.append(a['href'])
    return links
    
def FindArticles(url):
    url = url
    text = urllib2.urlopen(url).read()
    soup = BeautifulSoup(text)
    data = soup.findAll('div',attrs={'property':'rnews:articleBody'})
    textopuro = data[0].getText()
    return textopuro


