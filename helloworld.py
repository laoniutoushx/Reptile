import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.103 Safari/537.36 Vivaldi/2.1.1337.47'
}
res = requests.get('http://bj.xiaozhu.com/')
soup = BeautifulSoup(res.text, 'html.parser')
soup_res = soup.prettify
f = open('s:/121.txt','w+')
f.write(res.text)
try:
    print(soup_res)
except ConnectionError:
    print('拒绝连接')
f.close()