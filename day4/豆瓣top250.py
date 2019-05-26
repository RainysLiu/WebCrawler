import json
import os

import requests
from bs4 import BeautifulSoup


top250 = {}
for page in range(0,10):
    url = 'https://movie.douban.com/top250?start='+str(page*25)+'&filter='
    response = requests.get(url)
    response.encoding='utf8'
    pageresult = response.content
    su = BeautifulSoup(pageresult,'lxml')
    lidiv = su.find('ol',class_="grid_view").find_all('li')
    for li in lidiv:
        rank =int(li.find('em', class_="").text)
        title = li.find('span', class_="title").text
        imgurl = li.find('div', class_="pic").find('img')['src']
        info = li.find('p',class_="").text.replace('<br/>','\n')
        score = li.find('div',class_="star").find('span',class_="rating_num").text
        quotes = li.find('div',class_="star").find_all('span')[-1].text
        desc = li.find('p', class_="quote").text
        print(rank,imgurl,info,score,quotes,desc)
        top250[rank]={'电影名':title,'封面链接':imgurl,'信息':info,'评分':score,'评分人数':quotes,'简评':desc}
        fp = open(os.path.join('./豆瓣top250封面','top'+str(rank)+' '+title+'(评分'+score+').jpg'), 'wb' )
        fp.write(requests.get(imgurl).content)
jsString = json.dumps(top250, ensure_ascii=False)
fp = open('豆瓣top250电影.txt', 'w', encoding='utf8')
fp.write(jsString)




