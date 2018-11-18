# 爬取 妹子图 图片
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import time

web_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4',
}

img_headers = {
    'Host':'i.meizitu.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4',
    'Accept':'*/*',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://www.mzitu.com/',
    'Connection':'keep-alive',
}

download_links = []
path = 's:/photos/'

urls = ['http://www.mzitu.com/page/{}/'.format(str(i)) for i in range(200)]

for url in urls:
    res = requests.get(url,headers=web_headers)
    soup = BeautifulSoup(res.text, 'lxml')
    imgs = soup.select('li > a > img')

    for img in imgs:
        print(img.get('data-original'))
        download_links.append(img.get('data-original'))

    time.sleep(1)


for item in download_links:
    res = requests.get(item,headers=img_headers)
    fp = open(path + item[-10:],'wb')
    fp.write(res.content)
    fp.close()