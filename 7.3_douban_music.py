# 豆瓣音乐 top 250
import pymongo
from lxml import etree
import requests
import re
import time

client = pymongo.MongoClient('localhost', 27017)
mydb = client['test']
musictop = mydb['musictop']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4',
}

def get_info(url):
    res = requests.get(url,headers=headers)
    selector = etree.HTML(res.text)
    hrefs = selector.xpath('//a[@class="nbg"]/@href')
    for href in hrefs:
        get_detail(href)


def get_detail(href):
    res = requests.get(href,headers=headers)
    html = etree.HTML(res.text)

    title = html.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    player = html.xpath('//*[@id="info"]/span[1]/span/a/text()')[0]
    styles = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br', res.text, re.S)
    if len(styles) == 0:
        style = '未知'
    else:
        style = styles[0].strip()
    time = re.findall('发行时间:</span>&nbsp;(.*?)<br', res.text, re.S)[0].strip()
    publishers = re.findall('出版者:</span>&nbsp;(.*?)<br', res.text, re.S)
    if len(publishers) == 0:
        publisher = '未知'
    else:
        publisher = publishers[0].strip()
    
    score = html.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
    print(title, player, style, time, publisher, score)
    info = {
        'title':title,
        'player':player,
        'style':style,
        'time':time,
        'publisher':publisher,
        'score':score
    }
    musictop.insert_one(info)

if __name__ == "__main__":
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
    for url in urls:
        get_info(url)
        time.sleep(1)