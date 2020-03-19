# 抓取三十篇標題
import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/meme/posts?limit=30&before=233270957'
# 'https://www.dcard.tw/service/api/v2/forums/meme/posts?limit=100'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# print("\n")
json_string = str(soup)
js = json.loads(json_string)
print(js)
"""
# 抓取dict(涵蓋該網址內所有)及key值
for each_element in js:
    print(each_element)

for each_element in js[0]:
    print(each_element)
"""
"""
# 在字典裏面有id跟標題，剛好網址加id可以得到該網頁
for each_article in js:
    print(each_article['title'])
    print('https://www.dcard.tw/f/meme/p/'+ str(each_article['id']))
    print()

"""
##########################################################################################################
##########################################################################################################
##########################################################################################################
# 抓取三十篇標題 + 網址
import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/meme/posts?limit=30&before=233282925'
# 'https://www.dcard.tw/service/api/v2/forums/meme/posts?limit=100'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# print("\n")
json_string = str(soup)
js = json.loads(json_string)
# print(js)
"""
# 抓取dict(涵蓋該網址內所有)及key值
for each_element in js:
    print(each_element)

for each_element in js[0]:
    print(each_element)
"""

# 在字典裏面有id跟標題，剛好網址加id可以得到該網頁
for each_article in js:
    print(each_article['title'])
    print('https://www.dcard.tw/f/meme/p/'+ str(each_article['id']))
    print()

##########################################################################################################
##########################################################################################################
##########################################################################################################
# 抓取多頁 並 印出每篇文章裡的照片網址
import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/meme/posts?limit=30&before=233270957'
# 'https://www.dcard.tw/service/api/v2/forums/meme/posts?limit=100'

for i in range(0, 3):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    json_string = str(soup)
    js = json.loads(json_string)

    last_id = js[len(js)-1]['id']

    for each_article in js:
        # print(each_article['title'])
        print(each_article['title'], 'https://www.dcard.tw/f/meme/p/' + str(each_article['id']))
        for img_url in each_article['mediaMeta']:
            tmp_img_url = img_url['url']
            print('\t' + tmp_img_url)

        print()


    url = 'https://www.dcard.tw/service/api/v2/forums/meme/posts?limit=30&before=%s' % (last_id)
##########################################################################################################
##########################################################################################################
##########################################################################################################
# 抓取多頁 並 印出每篇文章裡的照片網址 並存在資料(老師的有錯)
import requests
from bs4 import BeautifulSoup
import json
import os
from urllib import request

res_path = r'./dcard_meme_pic2'
if not os.path.exists(res_path):
    os.mkdir(res_path)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=233281399'
# 'https://www.dcard.tw/service/api/v2/forums/meme/posts?limit=100'

for i in range(0, 2):

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    json_string = str(soup)
    js = json.loads(json_string)

    last_id = js[len(js)-1]['id']
    # 扁數命名
    k = 0
    for each_article in js:
        # print(each_article['title'])
        print(each_article['title'], 'https://www.dcard.tw/f/photography/p/' + str(each_article['id']))
        # 照片數
        n = 0

        for img_url in each_article['mediaMeta']:
            tmp_img_url = img_url['url']
            location = os.path.join(res_path + '/第%s篇_%s.jpg' % (k, n))
            # location = res_path + '/%s_%s.jpg' % (each_article['title'].replace('/', ''), n)
            n = n+1
            print(('\t' + tmp_img_url), end='')
            request.urlretrieve(tmp_img_url, location)
            print('\tdone')
        k = k+1
        print()
    url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=%s' % (last_id)
##########################################################################################################
## 抓取多頁 並 印出每篇文章裡的照片網址 並存在資料(我改變儲存方法)
import requests
from bs4 import BeautifulSoup
import json
import os
from urllib import request

res_path = r'./dcard_meme_pic2'
if not os.path.exists(res_path):
    os.mkdir(res_path)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=233281399'
# 'https://www.dcard.tw/service/api/v2/forums/meme/posts?limit=100'

for i in range(0, 2):

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    json_string = str(soup)
    js = json.loads(json_string)

    last_id = js[len(js)-1]['id']
    # 扁數命名
    k = 0
    for each_article in js:
        # print(each_article['title'])
        print(each_article['title'], 'https://www.dcard.tw/f/photography/p/' + str(each_article['id']))
        # 照片數
        n = 0

        for img_url in each_article['mediaMeta']:
            tmp_img_url = img_url['url']
            location = os.path.join(res_path + '/第%s篇_%s.jpg' % (k, n))
            # location = res_path + '/%s_%s.jpg' % (each_article['title'].replace('/', ''), n)
            n = n+1
            print(('\t' + tmp_img_url), end='')
            pic = requests.get(tmp_img_url) # 圖片網址
            img2 = pic.content  # 圖片裡的內容
            pic_out = open('./dcard_meme_pic2/第%s篇_%s.jpg' % (k, n), 'wb')  # img1.png為預存檔的圖片名稱
            pic_out.write(img2)  # 將get圖片存入img1.png
            pic_out.close()  # 關閉檔案(很重要)
            print('\tdone')
        k = k+1
        print()
    url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=%s' % (last_id)