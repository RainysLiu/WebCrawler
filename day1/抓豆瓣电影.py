import os

import requests
i=1
for m in range(0, 10):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start='+str(m*20)

    header = {

        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 60.0.3112.113Safari / 537.36'

    }

    html = requests.get(url, headers=header)



    html.encoding = 'utf-8'


    # 200

    # print(html.status_code)

    for n in range(20):
             # 图片网址

         url = html.json()['subjects'][n]['cover']
         print(url)

        # 用于取名字

        #urls = html.json()['data'][n]['thumbURL'][-20:]
        # 以二进制方式

         filename=str(i)+'.'+html.json()['subjects'][n]['title']+'(评分'+html.json()['subjects'][n]['rate']+').jpg'
         if '/' in filename:
           filename = str(i) + '.新世纪福音战士剧场版：Air真心为你(评分9.4).jpg'
         i+=1

         imagedata = requests.get(url).content

        # print(urls)


         with open(os.path.join(os.path.dirname(__name__),'豆瓣高分',filename), 'wb') as f:
            # 写入本地

            f.write(imagedata)
         print('电影’%s‘封面抓取成功！'%(filename))
