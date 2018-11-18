# 糗事百科用户地址
import requests
from lxml import etree
import csv
import json
import time

fp = open('s:/map.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('address', 'longitude', 'latitude'))

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4',
}

headers_details = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Referer':'https://www.qiushibaike.com/'
}

def get_user_url(url):
    url_part = 'http://www.qiushibaike.com'
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    url_infos = selector.xpath('//div[starts-with(@class,"article block untagged mb15")]')
    

    for url_info in url_infos:
        user_part_urls = url_info.xpath('div[1]/a[1]/@href')
        if len(user_part_urls) == 1:
            user_part_url = user_part_urls[0]
            get_user_address(url_part + user_part_url)
        else:
            pass

def get_user_address(address):
    print(address)
    res = requests.get(address,headers=headers_details)
    selector = etree.HTML(res.text)
    if selector.xpath('//div[@class="user-statis user-block"]/ul/li[4]/text()'):
        address = selector.xpath('//div[@class="user-statis user-block"]/ul/li[4]/text()')
        get_geo(address[1].split(' · ')[0] if len(address) > 1 else None)
    else:
        pass

def get_geo(address):
    print(address)
    if address == None:
        return
    par = {'address':address, 'key':'d9ff1d470bc55947962fe4064c1422c5'}
    api = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(api, par)
    json_data = json.loads(res.text)
    try:
        if json_data['status'] == '1':
            geo = json_data['geocodes'][0]['location']
            longitude = geo.split(',')[0]
            latitude = geo.split(',')[1]
            writer.writerow((address,longitude,latitude))
    except IndexError:
        pass

if __name__ == '__main__':
    urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 36)]
    for url in urls:
        get_user_url(url)
