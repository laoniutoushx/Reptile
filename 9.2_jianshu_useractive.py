# 简书 用户动态获取

import requests
from lxml import etree
import re
import pymongo

urls = ['https://www.jianshu.com/u/9104ebf5e177?order_by=shared_at&page={}'
    .format(str(i)) for i in range(1, 20)]

list = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.103 Safari/537.36 Vivaldi/'
}

for url in urls:
    print(url)
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    infos = selector.xpath('//ul[@class="note-list"]/li/html()')
    for info in infos:
        print(info)
        author = re.findall('<a class="nickname".*?>(.*?)</a>', info.text, re.S)
        print(author)
        title = re.findall('<a class="title".*?>(.*?)</a>', info.text, re.S)
        time = info.xpath('<span data-type="comment_note" data-datetime="(.*?)">', info.text, re.S)
        bean = {
            'author':author,
            'title':title,
            'time':time
        }
        print(bean)
        list.append(bean)

client = pymongo.MongoClient('localhost', 27017)
test = client['test']
jianshu_active = test['jianshu-active']

for item in list:
    jianshu_active.insert_one(item)