import time
from multiprocessing import Process

class SingProcess(Process):
    def __init__(self, name):
        # 手动调用父类
        super().__init__()
        self.name = name
    def run(self):
        for x in range(6):
            print('%s is sing a song'%self.name )
            time.sleep(1)
        print('唱歌进程结束')


class DanceProcess(Process):
    def __init__(self,name):
        #手动调用父类
        super().__init__()
        self.name = name
    def run(self):
        for x in range(6):
            print('%s is dancing'%self.name)
            time.sleep(1)
        print('跳舞进程结束')


def main():
    dname = '古丽娜扎'
    sname = '贺磊磊'
    p_sing = SingProcess(sname)
    p_dance = DanceProcess(dname)
    # 启动进程
    p_sing.start()
    p_dance.start()
    # 主进程在子进程结束之后再结束
    p_sing.join()
    p_dance.join()
    print('主进程结束')


if __name__ == '__main__':
    main()