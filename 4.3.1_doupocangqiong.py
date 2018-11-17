# 获取斗破苍穹网 全文小说
import requests
import re
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4'
}

f = open('s:/doupo.txt', 'a+')

def get_info(url):
    res = requests.get(url,headers=headers)
    if res.status_code == 200:             # 判断页面状态 跳过 404 页面
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content + '\n')
        else:
            pass

if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(num)) for num in range(1, 1665)]
    for url in urls:
        get_info(url)
        print(url)
        time.sleep(1)

f.close()