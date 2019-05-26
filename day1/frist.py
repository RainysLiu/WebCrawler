import urllib.request

import json

url = 'http://www.baidu.com'
imageurl = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?images&quality=100&size=b4000_4000&sec=1536570567&di=d00744579d95f122735eafeba1b9fc34&src=http://static.oeofo.com/201610/27/131242571000812.png'
response = urllib.request.urlopen(url)
result = response.read().decode()

print(json.dumps(result))


with open('baidu.html','w',encoding='utf8') as f:
    f.write(result)

imgresponse = urllib.request.urlopen(imageurl)
imgresult = imgresponse.read()


with open('girl.gif','wb') as f:
    f.write(imgresult)




