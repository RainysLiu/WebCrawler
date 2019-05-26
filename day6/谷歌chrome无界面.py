from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

path = r'E:\FeiQ文件\爬虫\day06\chromedriver_win32\chromedriver.exe'
# 创建谷歌浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

browser.get('http://www.baidu.com/')
time.sleep(3)

browser.save_screenshot('./pic/guge.png')
browser.quit()