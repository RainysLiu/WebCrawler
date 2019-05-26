import time

from multiprocessing import Process

import os

def sing(name):
    print('唱歌进程的id号为%s' % os.getpid())
    print('唱歌进程的父id号为%s' % os.getppid())
    for x in range(6):
        print('%s is sing a song'%name)
        time.sleep(1)
    print('唱歌进程结束')


def dance():
    print('跳舞进程的id号为%s' % os.getpid())
    print('跳舞进程的父id号为%s' % os.getppid())
    for x in range(6):
        print('Let’s dancing')
        time.sleep(1)
    print('跳舞进程结束')

def main():
    name = '贺磊磊'
    print('主进程的id号为%s'%os.getpid())
    #创建子进程,主进程可传参给子进程
    p_sing = Process(target=sing,args=(name,))
    p_dance = Process(target=dance)
    #启动进程
    p_sing.start()
    p_dance.start()
    #主进程在子进程结束之后再结束
    p_sing.join()
    p_dance.join()
    print('主进程结束')

if __name__ == '__main__':
    main() 