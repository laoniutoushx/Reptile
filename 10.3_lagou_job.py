# 拉勾网招聘信息

import requests
import time
import json
import pymongo

client = pymongo.MongoClient('localhost', 27017)
test = client['test']
lagou = test['lagou_interview']


url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%85%B0%E5%B7%9E&needAddtionalResult=false'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.113 Safari/537.36 Vivaldi/2.1.1337.51',
    'Cookie': 'WEBTJ-ID=20181129205137-1675f8650bf508-0a900181f27865-12121e13-1327104-1675f8650c1c1f; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543495897; _ga=GA1.2.1840287082.1543495898; user_trace_token=20181129205138-82b40bad-f3d5-11e8-86a4-525400f775ce; LGSID=20181129205138-82b40ead-f3d5-11e8-86a4-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0xeb752de800007348%26issp%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26oq%3D%2525E8%2525B1%252586%2525E7%252593%2525A3%26rsv_t%3D47cfhcfZJht7k0qKhsE0xR5LR%252BEDKnWjFI01q6mTozv1lfkUcUrhVziq6spjT0aOlxgl%26inputT%3D1746%26rsv_pq%3Dbfe3c45700006c2e%26rsv_sug3%3D18%26rsv_sug1%3D17%26rsv_sug7%3D100%26rsv_sug2%3D0%26rsv_sug4%3D1745; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20181129205138-82b41225-f3d5-11e8-86a4-525400f775ce; _gid=GA1.2.2053396495.1543495898; X_HTTP_TOKEN=08d2b8697379b02098560f5e8fe72efe; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221675f8668fa1bf-08a7dbe13fb6a2-12121e13-1327104-1675f8668fb203%22%2C%22%24device_id%22%3A%221675f8668fa1bf-08a7dbe13fb6a2-12121e13-1327104-1675f8668fb203%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=21192724ed0a7887f61920975014168f5302ea6586da84a7; _putrc=F827E06CBB4AC3AC; JSESSIONID=ABAAABAAAGGABCB7F8BE92D65796FA8F2F6489F9FE9EFF2; login=true; unick=%E5%B0%9A%E7%9A%93%E7%8E%BA; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=5; gate_login_token=bb5135a4a49ab7c34fc4b1ff0b574f287ea5b5b6888d1a46; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; _gat=1; SEARCH_ID=305abb28736e407cabea20286ed76edb; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543496971; LGRID=20181129210931-023fa364-f3d8-11e8-8c7b-5254005c3644',
    'Referer': 'https://www.lagou.com/jobs/list_?city=%E5%85%B0%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput='
}

def get_info(results):
    for result in results:
        infos = {
            'businessZones':result['businessZones'],
            'city':result['city'],
            'companyFullName':result['companyFullName'],
            'companyLabelList':result['companyLabelList'],
            'companySize':result['companySize'],
            'district':result['district'],
            'education':result['education'],
            'explain':result['explain'],
            'financeStage':result['financeStage'],
            'firstType':result['firstType'],
            'formatCreateTime':result['formatCreateTime'],
            'gradeDescription':result['gradeDescription'],
            'hitags':result['hitags'],
            'imState':result['imState'],
            'industryField':result['industryField'],
            'jobNature':result['jobNature'],
            'positionAdvantage':result['positionAdvantage'],
            'positionLables':result['positionLables'],
            'salary':result['salary'],
            'secondType':result['secondType'],
            'thirdType':result['thirdType'],
            'workYear':result['workYear']
        }
        lagou.insert_one(infos)

for i in range(1, 11):
    params = {
        'first': 'true' if i == 1 else 'false',
        'pn': i
    }

    res = requests.post(url, data=params, headers=headers)
    print(res.text)
    json_data = json.loads(res.text)
    get_info(json_data['content']['positionResult']['result'])
    

    time.sleep(2)

