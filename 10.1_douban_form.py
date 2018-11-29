# 登陆豆瓣

import requests

url = 'https://www.douban.com/accounts/login'

params = {
    'source':'index_nav',
    'form_email':'578585118@qq.com',
    'form_password':'6656200'
}

res = requests.post(url, params)
print(res.text)