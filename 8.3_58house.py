# 58 同城二手房
import requests
import re
from multiprocessing import Pool
from lxml import etree
import pymongo

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4',
}

def get_info(url):
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    house_info_urls = selector.xpath('//div[@class="pic"]/a/@href')
    for house_url_detail in house_info_urls:
        get_info_detail(house_url_detail)

def get_info_detail(house_url_detail):
    res = requests.get(house_url_detail, headers=headers)

    selector = etree.HTML(res.text)

    title = re.findall('<h1 class="c_333 f20">(.*?)</h1>')[0].strip()
    price = re.findall('<span class="price strongbox">(.*?)<b>万</b></span>')[0].strip()
    unit = re.findall('<span class="unit strongbox">(.*?)&nbsp;')[0].strip()
    room = re.findall('<p class="room">.*?<span class="main">(.*?)</span>')[0].strip()
    area = re.findall('<p class="area">.*?<span class="main">(.*?)</span>')[0].strip()
    community_1 = selector.xpath('//ul[@class="house-basic-item3"]/li[1]/span[2]/a[1]/text()')[0]
    community_2 = selector.xpath('//ul[@class="house-basic-item3"]/li[1]/span[2]/a[2]/text()')[0]
    community = community_1 + community_2

    address_1 = selector.xpath('//ul[@class="house-basic-item3"]/li[2]/span[2]/a[1]/text()')[0]
    address_2 = selector.xpath('//ul[@class="house-basic-item3"]/li[2]/span[2]/a[2]/text()')[0]
    address = address_1 + address_2

    info = {
        'title':title,
    }



def get_price(price):
    print(price)
    print()

if __name__ == "__main__":
    urls = ['https://lz.58.com/ershoufang/pn{}/'.format(str(i)) for i in range(1, 70)]
    for url in urls:
        get_info(url)