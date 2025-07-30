from threading import Thread,Lock  #导入线程模块
import time


def wdata():
    for i in range(5):
        li.append(i)
        time.sleep(0.1)
    print("写入的数据是",li)

def rdata():
    print("读取的数据是：",li)

if __name__ == "__main__":
    #创建子线程
    t1=Thread(target=wdata,args=())#用元组来传参，只有一个元素的时候一定要加上逗号
                                    #用kwargs来传参:用字典
    t2=Thread(target=rdata)
    t1.daemon(True)     #守护线程，必须放在start前面，主线程执行结束，子线程也会跟着结束
    #开启子线程
    t1.start()
    t1.name='fd'
    print(t1.name)
    t2.start()


li=[]       #定义全局变量


#写入数据
def wdata():
    for i in range(5):
        li.append(i)
        time.sleep(0.1)
    print("写入的数据是",li)

def rdata():
    print("读取的数据是：",li)

if __name__ == "__main__":
    #创建子线程
    t1=Thread(target=wdata)
    t2=Thread(target=rdata)

    #开启子线程
    t1.start()

    #阻塞线程
    t1.join()  #加入了join()只有一个线程运行完成之后才会运行下一个线程


    t2.start()


# 资源竞争
l=Lock()
l.acquire()
a=0
b=100000
def add():
    for i in range(b):
        global a    #要声明a为全局变量的a
        a+=1
        
    print("第一次",a)

def add2():
    for i in range(b):
        global a    #要声明a为全局变量的a
        a+=1
    print("第二次",a)

if __name__ =='__main__':
    first=Thread(target=add)
    second=Thread(target=add2)
    first.start()
    second.start()
l.release()
a=0
#线程同步:
# 两种方式:阻塞(见上面)  互斥锁(对共享的数据进行锁定)(见下面)

#创建互斥锁

def add():
    l.acquire()
    for i in range(b):
        global a    
        a+=1
    print("第一次",a)
    l.release()      #死锁:会造成其他任务等待，不会运行其他程序

def add2():
    l.acquire()
    for i in range(b):
        global a    #要声明a为全局变量的a
        a+=1
    print("第二次",a)
    l.release()

if __name__ =='__main__':
    first=Thread(target=add)
    second=Thread(target=add2)
    first.start()
    second.start()



#进程状态:
# 就绪状态
# 执行状态
# 阻塞状态 如一个程序sleep

# 进程语法结构
# multiprocessing模块提供了Process类代表进程对象
# Process 类参数
# target 执行的目标任务名
# args 以元组形式传参
# kwargs 以字典形式传参

# start()开启子进程
# is_alive()：判断是否存活
# join 主进程等待子进程执行结束
# 常用属性
# name：当前进程的别名 默认Process-N
# pid:当前进程的编号

from multiprocessing import Process,Queue
import os
def sing(name):
    print(os.getpid())  #获取此进程的id
    print(os.getppid()) #获取父进程的id
    print("唱歌"+name)
def dance(name):
    print(os.getpid())
    print("跳舞"+name)
if __name__=="__main__":
    p1=Process(target=sing,name='子进程1',args=('hhh',))    #传参用元组，传一个参数的时候要加上逗号
    p2=Process(target=dance,args=('fds',))

    p1.start()
    p2.start()
    print("p1",p1.name)
    print('p2',p2.name)
    p1.name='Process-1'
    print('p1',p1.name)

    print('p1',p1.pid)
    print('p2',p2.pid)
    
    print("主进程的编号",os.getpid())
    print("主进程的父进程编号",os.getppid())        #就是vs的进程

# 进程间不共享全局变量

a=[]
def w():
    global a
    for i in range(5):
        a.append(i)
    print("写完了",a)
def r():
    global a
    print('读取:',a)

if __name__ == '__main__':
    p1=Process(target=w)
    p2=Process(target=r)
    p1.start()
    p1.join()
    p2.start()
    p2.join()

if __name__ == '__main__':
    print("进程不共享全局变量")
    p1=Process(target=w)
    p2=Process(target=r)
    p1.start()
    p1.join()
    p2.start()
    p2.join()
#使用q队列进行信息通信:
# q.put()     放入数据
# q.get()     取出数据
# q.empty()   判断队列是否为空
# q.qsize()   返回当前队列包含的信息量
# q.full()    判断队列是否满了

#初始化一个队列队形
# from queue import Queue as Q
# q=Queue(3)      #代表最多可以接受3条信息，没写或者是一个负值就代表可以一直接受，直到队列尽头
# q.put("1")
# q.put("2")
# q.put("3")
# print(q.get())  #取出数据会将数据从q中移除
# print(q.get())
# print(q.get())
a=['张三','li4','wang5','zhao6']
def w1(q1):
    global a
    for i in range(5):
        q1.put(i)
        print(f"{i}已经被放入")
def r1(q2):
    global a
    while True:
        if q2.empty():
            break
        else:
            print("取出数据",q2.get())
if __name__=="__main__":
    q=Queue()
    p2_1=Process(target=w1,args=(q,))
    p2_2=Process(target=r1,args=(q,))
    p2_1.start()
    p2_1.join()
    p2_2.start()



#多线程io密集型,多进程cpu密集型(如高清解码,计算圆周率65\
