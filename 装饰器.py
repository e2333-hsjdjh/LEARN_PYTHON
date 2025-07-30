#第一种装饰器:
def decorator(func):
    def inner():
        return "hhh"+func()+'hhh'
    return inner

def a():
    return "lllll"

print(decorator(a)())  # 输出: hhhhhh


#第二种装饰器__语法糖
@decorator #注意不能加括号
def b():
    return "啦啦啦啦"
print(b())


def decorator_2(func):
    def inner(*args, **kwargs):
        return "装饰器开始"+func(*args, **kwargs)+"装饰器结束"
    return inner

@decorator_2
@decorator
def c():
    return "装饰器嵌套"
print(c())  # 输出: 装饰器开始 hhh装饰器嵌套hhh 装饰器结束


#有参数的装饰器:
def de(func):
    def inner(*args, **kwargs):
        return "装饰器开始"+str(func(*args, **kwargs))+"装饰器结束"
    return inner
def add(a):
    if isinstance(a, list):
        return sum(a)
    else:
        raise TypeError("参数必须是列表")

print(de(add)([1, 2, 3, 4]))  
