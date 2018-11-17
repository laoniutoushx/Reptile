# 糗事百科段子
import requests
import re
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4'
}

info_lists = []

def judgement_sex(class_name):
    if class_name == 'women':
        return '女'
    else:
        return '男'

def get_info(url):
    resp = requests.get(url, headers=headers)
    ids = re.findall('<h2>(.*?)</h2>', resp.text, re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', resp.text, re.S)
    sexs = re.findall('<div class="articleGender (\w+)Icon">', resp.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', resp.text, re.S)
    for id, level, sex, content in zip(ids, levels, sexs, contents):
        info = {
            'id':id,
            'level':level,
            'sex':judgement_sex(sex),
            'content':content,
        }
        info_lists.append(info)

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/8hr/page/{}/'.format(num) for num in range(1, 36)]
    for url in urls:
        print(url)
        get_info(url)
        time.sleep(1)

    f = open('s:/qiu_shi_bai_ke.txt', 'a+')
    for info_list in info_lists:
        try:
            f.write(info_list['id'] + '\n')
            f.write(info_list['level'] + '\n')
            f.write(info_list['sex'] + '\n')
            f.write(info_list['content'] + '\n')
        except Exception:
            pass
    f.close()
