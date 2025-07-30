#迭代器：(iterator)
#1.可迭代对象Iterable
#遍历(迭代):依次把对象中的一个个元素取出来的过程
#数据类型：str/list/tuple/dict/set
#条件：
#对象实现了__iter__()方法
#__iter__()返回了可迭代对象
#for循环工作原理:
#1.__iter__()返回可迭代对象迭代器  2.对获取到的迭代器不断__next__()方法获取下一个值将其赋值给临时变量

#判度是否是可迭代对象
from collections.abc import Iterable
o=(1,2,3)
t=Iterable
print(isinstance(o,t))  #o对象，t:类型

#迭代器是一个可以记住遍历位置的对象，在上次停留的位置做一些事情
#创建迭代器对象:
li=iter(o)  #或者 li=o.__iter__()
print(li)

#获取下一条参数:
print(next(li))#li2.__next__()
print(next(li))
print(next(li))
try:
    print(next(li))
except StopIteration as e:
    print (f'{e}'+'   迭代器已经取遍所有')


# 自定义迭代器类
# 要有两个属性
class Test:                 #此类只是一个普通是类
    def __init__(self):
        self.num=1
    def funa(self):
        print(self.num)
        self.num+=1
te=Test()
for i in range(0,5):
    te.funa()



class MyIterator:           #此类是一个迭代器类
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num==10:
            raise StopIteration("终止迭代")
        self.num+=1
        return self.num
mi=MyIterator()
for i in mi:
    print(i)



#生成器：
#列表中的元素后面的元素太占用位置，用生成器可以避免占用过多空间

li=[i*32 for i in range(5)] #列表推导式
gen=(i*32 for i in range(5))#变成了生成器
print(li)
print(gen)
print((next(gen)))
print((next(gen)))
print((next(gen)))

# python中使用了yield关键字的函数称之为生成器
# yeild作用：
# 类似return，将指定值或多个值返回给调用者
# vield语句一次返回一个结果，在每个结果中间挂起函数，执行next（）再重新从挂起点执行
def test():     #普通函数
    li=[]
    li.append('a')
    li.append('b')
    print('li',li)
test()
test()

def gen():     #生成器函数
    yield 'a'
    yield 'b'
gen_1=gen()
print(gen_1)
print(next(gen_1))
print(next(gen_1))
print(next(gen()))
print(next(gen()))
print(next(gen()))

def gen2(n):
    li=[]
    a=0
    while a<n:
        li.append(a)
        yield a
        a+=1
    print("li:",li)
print(gen2(5))
for i in gen2(5):
    print(i)


#可迭代对象指的是实现了python迭代协议，可以通过for in 循环遍历的对象，包含迭代器
#迭代器可以记住自己的位置，只能往前，不能往后，
#生成器是特殊的迭代器