# 爬取北京地区短租房信息
from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' + 
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.103 Safari/537.36 Vivaldi/2.1.1337.47'
}

def judgment_sex(class_name):   # 判断用户性别
    if class_name == ['member_icol']:
        return '女'
    else:
        return '男'

def get_links(url):             # 获取详细页 URL 的函数
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get('href')
        get_info(href)      # 获取网页信息

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    tittles = soup.select('div.pho_info > h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart > .day_l > span')
    imgs = soup.select('.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for tittle, address, price, img, name, sex in zip(tittles, addresses, prices, imgs, names, sexs):
        data = {
            'tittle':tittle.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text().strip(),
            'img':img.get('src'),
            'name':name.get_text(),
            'sex':judgment_sex(sex.get('class'))
        }
        print(data)

if __name__ == '__main__':  # 程序入口
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1, 14)]
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)



