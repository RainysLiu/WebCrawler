import json
from queue import Queue
import threading
import time
import requests
from bs4 import BeautifulSoup



class CrawlThread(threading.Thread):
    def __init__(self, name, page_queue, data_queue):
        super().__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/latest-{}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
    def run(self):
        print('%s线程启动------' % self.name)
        while 1:
            if self.page_queue.empty():
                break
            page = self.page_queue.get()
            print('进入获取页面%s' % page)
            url = self.url.format(page)
            r = requests.get(url=url, headers=self.headers,timeout=5)
            self.data_queue.put(r.text)
        print('%s线程结束--' % self.name)



class ParseThread(threading.Thread):
    def __init__(self, name, data_queue,lock,fp):
        super().__init__()
        self.name = name
        self.data_queue = data_queue
        self.lock = lock
        self.fp = fp
    def run(self):
        time.sleep(3)
        print('%s线程启动------' % self.name)
        while 1:
            if self.data_queue.empty():
                break
            content = self.data_queue.get()
            self.parse_content(content)
            print('页面解析完成')
        print('%s线程结束--' % self.name)
    def parse_content(self, content):
        soup = BeautifulSoup(content, 'lxml')
        # 解析即可
        ul = soup.find('ul',class_="cont-list")
        lilist = ul.find_all('li', class_="cont-item")
        for li in lilist:
            username = li.find('a', class_="user-head")['title']
            title = li.find('h2', class_="cont-list-title").text
            desc = li.find('div', class_="cont-list-main").text
            try:
                tucao = li.find('div', class_="cont-list-tc").text
            except:
                tucao =' '
            info = li.find('div', class_="cont-list-info fc-gray").text
            detailurl = li.find('div', class_="cont-list-sub clearfix").find('a', class_="fc-blue")['href']
            result = {'用户':username,'标题':title,'简介':desc,'吐槽':tucao,'发表信息':info,'详情页面':detailurl}
            print(result)
            self.lock.acquire()
            # 写入文件
            self.fp.write(json.dumps(result, ensure_ascii=False))
            self.lock.release()

# 创建队列函数
def create_queue():
    page_queue = Queue()
    for page in range(1, 10+1):
        page_queue.put(page)
    data_queue = Queue()
    return page_queue, data_queue

def main():
    page_queue, data_queue = create_queue()
    # 打开文件
    fp = open('fanjian.txt', 'w', encoding='utf8')
    lock = threading.Lock()
    # 创建列表，用来保存所有的线程
    t_crawl_list = []
    t_parse_list = []
    # 创建所有的采集线程，并且启动之
    crawl_names_list = ['采集线程1', '采集线程2', '采集线程3']
    for crawl_name in crawl_names_list:
        t_crawl = CrawlThread(crawl_name, page_queue, data_queue)
        t_crawl_list.append(t_crawl)
        t_crawl.start()
    # 创建所有的解析线程，并且启动之
    parse_names_list = ['解析线程1', '解析线程2', '解析线程3']
    for parse_name in parse_names_list:
        t_parse = ParseThread(parse_name, data_queue, lock,fp)
        t_parse_list.append(t_parse)
        t_parse.start()
    # 主线程等待子线程
    for t_crwl in t_crawl_list:
        t_crwl.join()
    for t_par in t_parse_list:
        t_par.join()
    fp.close()
    print('主线程-子线程全部结束')

if __name__ == '__main__':
    main()
