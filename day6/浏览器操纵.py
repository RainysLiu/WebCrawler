import time

from selenium import webdriver




path = r'E:\工作区\WebCrawler\day6\chromedriver_win32\chromedriver.exe'
# 创建谷歌浏览器对象
browser = webdriver.Chrome(executable_path=path)

# 通过浏览器对象上网
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(1)

# 找到输入框，往里面写内容
my_input = browser.find_element_by_id('kw')
# 往里面写内容
my_input.send_keys('毛主席')
time.sleep(1)

# 点击百度一下按钮
my_button = browser.find_element_by_id('su')
my_button.click()
time.sleep(3)

#//*[@id="1"]/h3/a
a_href = browser.find_elements_by_xpath('//*[@id="2"]/h3/a')[0]
a_href.click()
time.sleep(20)




# 退出浏览器
browser.quit()
