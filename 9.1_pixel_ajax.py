# PIXELS ajax 下载图片
import requests
from lxml import etree

headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.103 Safari/537.36 Vivaldi/2.1.1337.47',
    'referer': 'https://www.pexels.com/'
}
urls = ["https://www.pexels.com/?page={}".format(str(i)) for i in range(1, 20)]
list = []
for url in urls:
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    img_urls = selector.xpath('//div[@class="photos"]/article/a/img/@src')
    for img_url in img_urls:
        list.append(img_url)

path = 'S://pixels/'

for item in list:
    data = requests.get(item, headers=headers)
    print(item)
    fp = open(path + item.split('?')[0][-10:], 'wb')
    fp.write(data.content)
    fp.close()
