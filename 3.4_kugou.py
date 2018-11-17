from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.4'
}

def get_info(url):
    wb = requests.get(url,'lxml')
    soup = BeautifulSoup(wb.text)
    ranks = soup.select('.pc_temp_num')
    title = soup.select('.pc_temp_songname')
    lengths = soup.select('.pc_temp_time')
    for rank, title, length in zip(ranks, title, lengths):
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().split('-')[0],
            'song': title.get_text().split('-')[1] if len(title.get_text().split('-')) > 1 else '',
            'time': length.get_text().strip(),
        }
        print(data)
    
if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1, 24)]
    print(urls)
    time.sleep(5)

for url in urls:
    print(url)
    get_info(url)
    time.sleep(1)