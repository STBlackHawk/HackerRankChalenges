#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackerRank: Deteck HTML links

@author: blackhawk
"""


#We have to either user Regex or we need to scape from HTML entities like &amp


from bs4 import BeautifulSoup
from xml.sax.saxutils import escape


def HtmlLinks(Html):
    soup = BeautifulSoup(Html, 'html.parser')
    links = soup.find_all('a')
    return((escape(link.get('href')),link.get_text().strip()) for link in links)
        



if __name__=='__main__':
    import sys
    for link, text in HtmlLinks(sys.stdin.read()):
        print('{},{}'.format(link, text))

