# cookie 模拟登陆

import requests
url = 'https://www.douban.com/'

headers = {
    'Cookie': 'bid=snj5Q_YH1Z4; __utmc=30149280; douban-fav-remind=1; __utmv=30149280.6682; ap_v=0,6.0; push_doumail_num=0; __utma=30149280.1585592898.1531562958.1543492736.1543494763.13; __utmz=30149280.1543494763.13.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; douban-profile-remind=1; __utmb=30149280.6.10.1543494763; ps=y; push_noty_num=3; as="https://www.douban.com/people/66827739/"'
}

res = requests.get(url, headers = headers)

print(res.text)