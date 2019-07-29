import feedparser
import pprint as pp

# rss_oschina = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
rss_oschina = feedparser.parse('https://www.oschina.net/news/rss')
mylist = [{'title':entry['title'], 'link':entry['link']} for entry in rss_oschina['entries']]
pp.pprint(mylist)

