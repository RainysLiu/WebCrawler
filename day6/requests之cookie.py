import requests

# 创建一个会话,往下的所有get-post请求都要使用s进行发送
# s.get()   s.post()

s = requests.Session()

# 在往下所有的请求都使用opener.open()方法发送，那么就会自动保存cookie和携带cookie

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201883115448'

formdata = {
	'email': '17701256561',
	'icode': '',
	'origURL': 'http://www.renren.com/home',
	'domain': 'renren.com',
	'key_id': '1',
	'captcha_type': 'web_login',
	'password': '416f0c7ccd370d88b6c15b1bbff0f328583a8bce638bada6b5b3b345696c4c35',
    'rkey': 'cac8af90965f6d9819e7956057ea478d',
	'f': 'http%3A%2F%2Fwww.renren.com%2F960481378%2Fprofile',
}


headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

r = s.post(post_url, data=formdata)
print(r.text)

# 访问登录后的页面
pro_url = 'http://www.renren.com/960481378/profile'
res = s.get(url=pro_url, headers=headers)

with open('renren2.html', 'wb') as fp:
	fp.write(res.content)

