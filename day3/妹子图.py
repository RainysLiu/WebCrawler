import os
import requests
import re

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,images/webp,images/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    'Connection': 'keep-alive',
    "Referer": "http://www.mzitu.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }

i=1
pages = int(input('请告诉我你需要少页妹子（每页24个）:'))
for page in range(1,pages+1):
    url = 'http://www.mzitu.com/page/'+str(page)+'/'
    print('*******第%s页开始爬取。。。*******'%page)
    result = requests.get(url,headers=header)
    result.encoding= 'utf8'
    data = result.text
    ulrule ='<ul id="pins">(.*?)</ul>'

    ulresult = re.findall(ulrule,data,re.S)[0]
    print(ulresult)

    imgalt = "alt='(.*?)'"
    image_original = "data-original='(.*?)'"
    imgurllist = re.findall(image_original,ulresult)
    imgtitlelist = re.findall(imgalt,ulresult)
    print('本页所有图片地址：',imgurllist)
    print('本页所有图片标题：',imgtitlelist)

    for x in range(len(imgtitlelist)):
        img = requests.get(imgurllist[x],headers=header).content
        imgname = str(i)+'.'+imgtitlelist[x]+'.jpg'
        i += 1
        f = open(os.path.join(os.path.dirname(__name__), '妹子图', imgname), 'wb') # 写入本地
        f.write(img)
        print('%s爬取成功'%imgname)
    print('*******第%s页爬取结束！！！*******' % page)
