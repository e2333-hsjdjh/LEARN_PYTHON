

def check_unsafe_words(comments):
    """this function is used for checking if the sentence involve given-string
    参数：
    coments:
    
    """
    if "TMD" in comments:
        return"不通过"
    else:
        return"通过"
#return后面的代码将不再执行，并且其如果不跟其他变量等，将会返回 none
a=input("请输入")
print(check_unsafe_words(a))

def calc_square_and_cube(n):
    """this function is used for calculating the square and cube of a number
    参数：
    n: the number to be calculated
    """
    return n,n**2, n**3
#调用函数
result,n,m = calc_square_and_cube(3)
print("n:", result)
print("n的平方:", n)    
print("n的立方:", m)
def creat_game_character(username,email,level=1):
    """this function is used for creating a game character
    参数：
    username: the name of the character
    email: the email of the character
    level: the level of the character, default is 1
    """
    return f"角色名：{username}, 邮箱：{email}, 等级：{level}"

#调用函数(关键词传参)
character = creat_game_character(username="hero",level=5, email="fdagfda")
print(character)

def add(a, b):
    """this function is used for adding two numbers
    参数：
    a: the first number
    b: the second number
    """
    return a + b
def subtract(a, b):
    """this function is used for subtracting two numbers
    参数：
    a: the first number
    b: the second number
    """
    return a - b
def multiply(a, b):
    """this function is used for multiplying two numbers
    参数：
    a: the first number
    b: the second number
    """
    return a * b 
def divide(a, b):
    """this function is used for dividing two numbers
    参数：
    a: the first number
    b: the second number
    """
    if b == 0:
        return "除数不能为0"
    return a / b
def calculator(a, b, operation):
    """this function is used for calculating two numbers
    参数：
    a: the first number
    b: the second number
    operation: the operation to be performed, can be add, subtract, multiply, divide
    """
    return operation(a, b)
#调用函数
result = calculator(10, 5, add)
print("计算结果:", result)  
result = calculator(10, 5, subtract)
print("计算结果:", result)      

result = calculator(10, 5, multiply)
print("计算结果:", result)
result = calculator(10, 5, divide)
print("计算结果:", result)  
result = calculator(10, 0, divide)
print("计算结果:", result)
#参数也可以是函数


#在函数外使用函数内的变量：global
def global_variable_example():
    """this function is used for demonstrating the use of global variable"""
    global x
    x = 10
    return x

#nonlocal变量:只能在嵌套函数中使用
def outer_function():
    """this function is used for demonstrating the use of nonlocal variable"""
    y = 5
    def inner_function():
        nonlocal y
        y += 1
        return y
    return inner_function()


#匿名函数
add = lambda x, y: x + y

#内置函数：
abs(-10)  # 绝对值
sum([1, 2, 3, 4])  # 要放可迭代对象
max([1, 2, 3, 4])  # 最大值
min([1, 2, 3, 4])  # 最小值
zip([1, 2, 3], ['a', 'b', 'c'])  # 打包成元组
# map函数：对可迭代对象中的每个元素应用一个函数
mp=map(lambda x: x * 2, [1, 2, 3, 4])  # [2, 4, 6, 8]
for i in mp:
    print(i)
from functools import reduce
# reduce函数：对可迭代对象中的元素进行累积操作
rd=reduce(lambda x, y: x ** y, [9, 2, 3, 4])  # 函数只能是两个参数
print(rd)


#拆包:
ze=[1,2,3,4]
a, b, c, d = ze  # 拆包,要求对象内数据数和变量数相同
print(a, b, c, d)

a,*b = ze  # 拆包,要求对象内数据数大于变量数
print(a, b)  # a=1, b=[2, 3, 4]


def fun(a,b,*c):
    print(*c)
    print(type(c))
fun(1,2,3,4,4,5,6,67,7)

#递归函数:
def fabo(n):
    if n<=1:
        return n 
    return fabo(n-1) + fabo(n-2)
print(fabo(10))  # 输出第10个斐波那契数


#闭包：
def outer_function(x):
    """this function is used for demonstrating the use of closure"""
    def inner_function(y):
        return x + y
    return inner_function
print(outer_function(10)(5))  # 输出15

a_1= outer_function(10)  # 返回inner_function函数
print(a_1(5))  # 输出15
print(a_1(10))  # 输出20