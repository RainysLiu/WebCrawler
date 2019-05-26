from selenium import webdriver
import time

url = 'https://images.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
path = r'E:\工作区\WebCrawler\day6\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# 创建浏览器对象
browser = webdriver.PhantomJS(executable_path=path)

browser.get(url)
time.sleep(3)

browser.save_screenshot('./pic/美女1.png')

# 模拟滚动条到底部, 第二个可以写body，也可以写documentElement
js = 'document.body.scrollTop=10000'
# 让phantomjs执行这个代码
browser.execute_script(js)
time.sleep(4)
browser.save_screenshot('./pic/美女2.png')

# 得到执行完js之后的代码
# browser.page_source
# with open('douban.html', 'w', encoding='utf8') as fp:
# 	fp.write(browser.page_source)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(browser.page_source, 'lxml')


browser.quit()