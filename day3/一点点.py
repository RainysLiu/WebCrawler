import os

import requests
from bs4 import BeautifulSoup
import re

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,images/webp,images/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "www.yikexun.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }
i=1
pages = int(input('请告诉我你需要少页语录(每页15个):'))
for page in range(1,pages+1):
    url = 'http://www.yikexun.cn/niandujingdianyulu/list_24_'+str(page)+'.html'
    print('*******第%s页开始爬取。。。*******'%page)
    result = requests.get(url,headers=header)
    result.encoding= 'utf8'
    data = result.text
    #print(data)
    ulrule ="<ul class='art-ul'>(.*?)</ul>"
    ulresult = re.findall(ulrule,data,re.S)[0]
    title = '<h3><a href=".*?">(.*?)</a></h3>'
    contenturl = '<h3><a href="(.*?)">.*?</a></h3>'
    art_title = re.findall(title,ulresult,re.S)
    art_content = re.findall(contenturl, ulresult,re.S)
    for x in range(len(art_title)):
        titlle = art_title[x]
        try :
            titlle = re.findall(r'<b>(.*?)</b>',titlle)[0]
        except:
            pass
        print('正在爬取文章《%s》......' % titlle)
        artURL = 'http://www.yikexun.cn'+art_content[x]
        print('内容链接:',artURL)
        artresult = requests.get(artURL,headers=header)
        artresult.encoding = 'utf8'
        artdata = artresult.content
        soup = BeautifulSoup(artdata,'lxml')
        neirong_div = soup.find('div', class_='neirong')
        pdiv = neirong_div.find_all('p')
        content = ''
        for x in range(len(pdiv)):
            content += pdiv[x].get_text()+'\n'
        f = open(os.path.join(os.path.dirname(__name__), '年度经典语录', str(i)+'.' +titlle +'.txt'), 'wb')  # 写入本地
        f.write(content.encode('utf8'))
        print('文件“',str(i)+'.' +titlle +'.txt','”已经写入本地成功！...')
        i += 1
    print('*******第%s页爬取结束。。。*******' % page)



