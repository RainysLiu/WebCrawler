import os

import requests
i=1
for m in range(0, 10):
    url = 'https://images.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&cg=girl&pn='+\
          str(m*30)+'&rn=30&gsm=1e&1536582525430='

    header = {

        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 60.0.3112.113Safari / 537.36'

    }

    html = requests.get(url, headers=header)

    # 解决乱码问题

    html.encoding = 'utf-8'

    print(html.json())

    # 200

    # print(html.status_code)

    for n in range(30):
             # 图片网址


         url = html.json()['data'][n]['thumbURL']
         print(url)

        # 用于取名字
        # 以二进制方
         filename='美女'+str(i)+'号.jpg'
         i+=1

         data = requests.get(url).content

        # print(urls)
         if not os.path.exists('美女'):
             os.mkdir('美女')


         with open(os.path.join(os.path.dirname(__name__),'美女',filename), 'wb') as f:
            # 写入本地

            f.write(data)
         print('第%d号美女抓成功！'%(i-1))





