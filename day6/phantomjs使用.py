from selenium import webdriver
import time

path = r'E:\工作区\WebCrawler\day6\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# 创建浏览器对象
browser = webdriver.PhantomJS(executable_path=path)

url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)

# 拍个照片，留个纪念
browser.save_screenshot('./pic/baidu.png')
# 打开输入框，输入美女
browser.find_element_by_id('kw').send_keys('美女')
time.sleep(3)

browser.find_element_by_id('su').click()
time.sleep(3)
browser.save_screenshot('./pic/baidu1.png')

browser.quit()