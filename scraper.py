# Code from Ross Jones https://classic.scraperwiki.com/scrapers/google_news_scrape_1/index.html
# Changed search term and number of results at bottom of code

import urllib2
from xml.dom.minidom import parseString

def get_google_new_results( term, count ):
    results = []
    obj = parseString( urllib2.urlopen('http://news.google.com/news?q=%s&output=rss' % term).read() )

    items = obj.getElementsByTagName('item') # Get each item
    for item in items[:count]:
        t,l = '', ''
        for node in item.childNodes:
            if node.nodeName == 'title':
                t = node.childNodes[0].data
            elif node.nodeName == 'link':
                l = node.childNodes[0].data
        results.append( (t,l) )
    return results


items = get_google_new_results( 'catksill+mountains', 9 )
# items is a list where each element is a tuple (title, link,)
for title,link in items:
    print title, '', link
