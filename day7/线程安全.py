import threading

count = 100
#创建锁
lock = threading.Lock()


def demo(num):
    global count
    for x in range(0,1000000):
        lock.acquire()
        count +=num
        count -= num
        lock.release()
    print('%s线程结束后的值为%s'%(threading.current_thread().name,count))
def main():
    t1 = threading.Thread(target=demo,args=(3,))
    t2 = threading.Thread(target=demo,args=(5,))

    # 启动线程
    t1.start()
    t2.start()
    # 主线程
    t1.join()
    t2.join()
    print('主线程/子线程全部结束！')


if __name__ == '__main__':
    main()