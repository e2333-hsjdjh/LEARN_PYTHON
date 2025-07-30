#协程是python特有的，单线程下的开发，由称为单线程
# 注意：线程和进程是由程序触发系统接口，最后执行者是系统，协程的操作者是程序员
# 简单实现协程
from time import sleep
# def task1():
#     while True:
#         yield 1
#         sleep(1)
# def task2():
#     while True:
#         yield 2
#         sleep(1)
# if __name__=='__main__':
#     t1=task1()
#     t2=task2()
#     while True:
#         print(next(t1))
#         print(next(t2))

# 应用场景:
# 如果一个线程里有io操作比较多的时候 可以用协程
# 文件操作,网络请求
# 适合高并发处理


# greenlet是一个由C语言实现的协程模块,通过设置switch()来实现任意函数之间的切换
# 属于手动切换,遇到io操作,程序会堵塞
# 通过greenlet实现任务的切换
print(0)
from greenlet import greenlet
def sing():
    print("在唱歌")

    g2.switch()
    
    print("唱完歌了")
def dance():
    print("在跳舞")
    
    print("跳完舞了")
    
    g1.switch()

if __name__=='__main__':
    g1=greenlet(sing)
    g2=greenlet(dance)

    g1.switch()


print(1)
# gevent 模块,自动切换,主动式切换
# gevent遇到io操作时会自动切换
import gevent
# gevent.spawn(函数名):创建协程对象
# gevent.sleep():耗时操作
# gevent.join():阻塞,等待某个协程执行结束
# gevent.joinall()等待所有协程对象都执行后退出,参数是一个协程对象列表
def sing1():
    print("在唱歌")

    gevent.sleep(3.1)    
    print("唱完歌了")
def dance1():
    print("在跳舞")
    gevent.sleep(3)    #两个是同时操作,先出现耗时少的,再完成耗时多的
    print("跳完舞了")
    


if __name__=='__main__':
    g1_1=gevent.spawn(sing1)
    g1_2=gevent.spawn(dance1)
    g1_1.join()     #等待g1对象结束
    

print(2)

def sing(name):
    for i in range(5):
        gevent.sleep(0.1)
        print(f"{name}在唱歌,这是第{i+1}次")
if __name__=='__main__':
    gevent.joinall([
        gevent.spawn(sing,"he"),
        gevent.spawn(sing,"she"),
        gevent.spawn(sing,"it"),
    ])

print(3)

#monkey补丁:拥有在模块运行时替换的功能
from gevent import monkey
monkey.patch_all()      #将用到的time.sleep()代码全部替换为自己实现耗时操作的gevent.sleep()


