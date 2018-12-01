# 新浪微博好友圈信息
# 词云制作
import requests
import json
import jieba.analyse

## 微博数据读取
headers={
    'Cookie':'_T_WM=375916800fb339d2cf9f31801b93a3dd; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000174; SUB=_2A25xBYkyDeRhGeBK4lQS8y3PyzuIHXVSCRd6rDV6PUJbkdANLUfmkW1NR3kz6AnftFq5oKup1_0Oh7ep3xQIUlvz; SUHB=0xnCfmZUZrlWBc; SCF=AmmRsSVdotl1KoVLSlQJWNnTRnaXRoiCLqD5KoG1liYuk-AdxBVG3voXg2mxjDAbFGu7J4A9wdp_RNrL0koP-fA.; SSOLoginState=1543633250',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate, br',
    'origin':'https://m.weibo.cn',
    'Connection':'keep-alive',
    'Host':'m.weibo.cn',
}

f = open('S:/weibo.txt', 'a+', encoding='utf-8')
# 创建 TXT 文件

def get_info(max_id, ttl):
    url = 'https://m.weibo.cn/feed/friends?max_id=' + str(max_id)
    print(url)
    res = requests.get(url,headers=headers)
    json_data = json.loads(res.text)
    
    statuses = json_data['data']['statuses']
    for statu in statuses:
        text = statu['text']
        f.writelines(text)

    if ttl == 20:
        return;
    cursor = json_data['data']['next_cursor']
    get_info(cursor, ttl = ttl + 1)

get_info('4312373911762824', 1)

# 词频分析

path = 'S:/weibo.txt'
fp = open(path, 'r', encoding='utf-8')
content = fp.read()
try:
    jieba.analyse.set_stop_words('S:/tingci.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    for item in tags:
        print(item[0] + '\t' + str(int(item[1] * 1000)))
finally:
    fp.close()