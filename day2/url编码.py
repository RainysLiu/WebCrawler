import urllib.parse


string = 'username=周杰伦'

ret = urllib.parse.quote('http://www.baidu.com/index.html?username=狗蛋')


print(ret)