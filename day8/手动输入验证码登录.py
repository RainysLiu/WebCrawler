

import requests
from bs4 import BeautifulSoup
s = requests.session()

headers={
    'authority': 'so.gushiwen.org',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,images/webp,images/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',

}

loginUrl = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

r = s.get(url=loginUrl,headers=headers)

suop = BeautifulSoup(r.text,'lxml')

imgSrc = 'https://so.gushiwen.org/'+suop.find('img',id ='imgCode')['src']
ImageResponse = s.get(imgSrc,headers=headers,timeout =5)
with open('codeImg.png','wb') as f:
    f.write(ImageResponse.content)


viewstate = suop.find('input',id='__VIEWSTATE')['value']
viewg = suop.find('input',id = '__VIEWSTATEGENERATOR')['value']

code = input('请输入验证码：')


data ={
'__VIEWSTATE': viewstate,
'__VIEWSTATEGENERATOR': viewg,
'from': 'http://so.gushiwen.org/user/collect.aspx',
'email': '1072799939@qq.com',
'pwd': 'la1414785769',
'code': code,
'denglu': '登录',
}
postUrl = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
r = s.post(postUrl,data=data,headers=headers,timeout = 3)
if '退出登录' in r.text:
    print('登录成功!')
else:
    print('验证码输入不正确，登陆失败！')
