import threading
import time


def sing(name):
    print('sing线程的名字为%s' % threading.current_thread().name)
    for x in range(6):
        print('%s is sing a song'%name)
        time.sleep(1)
    print('唱歌线程结束')


def dance():
    print('dance线程的名字为%s' % threading.current_thread().name)
    for x in range(6):
        print('Let’s dancing')
        time.sleep(1)
    print('跳舞线程结束')


def main():
    #主线程
    print('主线程的名字为%s' % threading.current_thread().name)
    #创建子线程
    t_sing = threading.Thread(target=sing,args=('贺磊磊',),name='唱歌')
    t_dance = threading.Thread(target=dance)
    #启动线程
    t_sing.start()
    t_dance.start()
    #主线程
    t_sing.join()
    t_dance.join()
    print('主线程/子线程全部结束！')
if __name__ == '__main__':
    main()
