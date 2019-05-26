import os
import time
from multiprocessing import Pool

def demo(name):
    print('当前任务名为--%s--，当前进程id为--%s--'%(name,os.getpid()))
    time.sleep(1)

def main():
    #创建一个进程池，进程池里最多三个进程
    pol = Pool(3)
    lt = ['贺磊磊','毛润之','蒋中正','特朗普','习近平','金正恩','安倍晋三','普京']
    for name in lt:
        #给进程池添加任务
        pol.apply_async(demo,args=(name,))
    #关闭进程池
    pol.close()
    pol.join()
    print('主进程/子进程全部结束！')

if __name__ == '__main__':
    main()