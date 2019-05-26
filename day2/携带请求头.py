import urllib.request



url = 'http://www.baidu.com'

header = {

    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 60.0.3112.113Safari / 537.36'

}

request = urllib.request.Request(url,headers=header)


reponse = urllib.request.urlopen(request)


print(reponse.read().decode('utf8'))