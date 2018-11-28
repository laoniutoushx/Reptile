# 简书 用户动态获取
import requests
from lxml import etree
import re
import pymongo


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.103 Safari/537.36 Vivaldi/'
}


client = pymongo.MongoClient('localhost', 27017)
mydb = client['test']   #  新建 test 数据库
test = mydb['jianshu_active']     # 新建 test 数据集合

def get_info(url, ttl):
    if ttl > 20: 
        return;
    new_url = url

    print(url)
    res = requests.get(url, headers=headers)
    authors = re.findall('<a class="nickname".*?>(.*?)</a>', res.text, re.S)
    titles = re.findall('<a class="title".*?>(.*?)</a>', res.text, re.S)
    times = re.findall('<span data-type="like_user" data-datetime="(.*?)">', res.text, re.S)

    
    # old_str = re.findall('max_id=(.*)', url, re.S)[0].strip()
    new_strs = re.findall('id="feed-(.*?)">', res.text, re.S)
    new_str = new_strs[len(new_strs) - 1]

    # new_url = new_url.replace(old_str, new_str)

    new_url = 'https://www.jianshu.com/users/9104ebf5e177/timeline?max_id=%s'%(new_str)

    ttl += 1

    for author, title, time in zip(authors, titles, times):
        print(author + ' - ' + title + ' - ' + time)
        test.insert_one({'author':author, 'title':title, 'time':time})

    get_info(new_url, ttl)
        

if __name__ == "__main__":
    get_info('https://www.jianshu.com/users/9104ebf5e177/timeline?max_id=381253419', 1)
