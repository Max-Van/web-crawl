# web-crawler
learn web crawler


### Install it 

~~~bash
$ pip install feedparser
$ pip install pprint 
~~~


### feedreader.py

~~~python
import feedparser
import pprint as pp

#
#print(feedparser.__version__)

#  网站种子解析
#rss_oschina = feedparser.parse('https://www.oschina.net/news/rss')
rss_oschina = feedparser.parse('http://rss.cnn.com/rss/edition.rss')

#抓取内容确认
#pp.pprint(rss_oschina, depth=1)

# 输出编码方式
# print('encoding:', rss_oschina.get('encoding'))
# print('encoding:', rss_oschina['encoding'])

# 新闻列表输出
# pp.pprint(rss_oschina['entries'], depth=2)

# 控制台输出
# for entry in rss_oschina['entries']:
#     print(entry['title'])
#     print('', entry['link'])
#     print('', entry['published'])

# 整理为数组
# titles = [entry['title'] for entry in rss_oschina['entries']]
# pp.pprint(titles)

# 整理为JSON数组
mylist = [{'title':entry['title'], 'link':entry['link']} for entry in rss_oschina['entries']]
pp.pprint(mylist)
~~~