import urllib.request


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,images/webp,images/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    'Connection': 'keep-alive',
    "Referer": "http://www.mzitu.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    }

imgurl = 'http://i.meizitu.net/thumbs/2018/09/150384_12b40_236.jpg'


request = urllib.request.Request(url=imgurl, headers=header)
response = urllib.request.urlopen(request)
result = response.read()
print(result)
f = open('mm.jpg','wb')
f.write(result)



