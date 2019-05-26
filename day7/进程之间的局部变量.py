import time
from multiprocessing import Process

def demo(name):
    count = 200
    if name == 'change':
        #修改count的值
        count += 50
        print('p1修改后的值为%s' % count)
    else:
        #读取count的值
        time.sleep(1)
        print('p2读取的值为%s'%count)

def main():
    p1 = Process(target=demo,args=('change',))
    p2 = Process(target=demo,args=('read',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('主进程/子进程全部结束！')


if __name__ == '__main__':
    main()