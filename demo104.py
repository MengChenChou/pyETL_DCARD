import requests
from bs4 import BeautifulSoup
# https://www.104.com.tw/jobs/search/?ro=1&keyword=資料科學家&area=6001001000&isnew=30&page=1&order=11

url = 'https://www.104.com.tw/jobs/search/?'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
# 限定全職的工作，如果不限定則輸入0,想要查詢的關鍵字,限定在台北的工作,只要最近一個月有更新的過的職缺,清單的瀏覽模式'mode':'l',kwop=1
my_params = {'ro':'1',
             'keyword':'資料科學家',
             'area':'6001001000',
             'isnew':'30',
             'page':'1',
             'mode':'l',
             'order':'11'}

res = requests.get(url, my_params, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
"""
title = soup.select('em[class="b-txt--highlight"]')
print(title[0].prettify())
"""

page = 1
k = 0
while page > 0:
    my_params = {'ro': '1',
                 'keyword': '資料科學家',
                 'area': '6001001000',
                 'isnew': '30',
                 'page': '%d' % page,
                 'mode': 'l',
                 'order': '11'}
    res = requests.get(url, my_params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    # print(soup.prettify())
    title = soup.select('li[class="job-mode__jobname"] a')
    if title == []:
        break
    for t in title:
        article_title = t.text
        article_url = 'https:' + t['href']
        print(article_title)
        print(article_url)
        k = k+1
    print(k)
    page = page + 1




