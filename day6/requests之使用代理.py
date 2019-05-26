import requests

url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
proxy = {
    'http': '120.92.74.189:3128'
}
r = requests.get(url=url, headers=headers, proxies=proxy)

with open('daili.html', 'w', encoding='utf8') as fp:
    fp.write(r.text)