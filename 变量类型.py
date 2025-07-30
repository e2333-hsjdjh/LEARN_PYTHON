"""
#python can autmetically design the type of zhe variate
a=b=111;c="dfahsui"
print(id(a),type(a))
print(id(b),type(b))
print(id(c),type(c))

#exchange two variate
d=10000
a,d=d,a
print(a,d)

#input more then one variate
e,f,g=eval(input("please input three words"))
print(e,f,g)

#the type of the integer
number=348
print(bin(number))  #二进制
print(oct(number))  #八进制
print(hex(number))  #十六进制

print(format(number,'b'))
print(format(number,'o'))
print(format(number,'x'))


#the type of float

#高精度:                    float
#复数：                     complex
#精确数值的小数，计算较慢：   decimal
h=8.9e-4
print(h)

i=542+4324j
print((455+9009j)+i)

print(type(i))

print(i.real,i.imag,i.conjugate)

from decimal import Decimal
print(0.12341*222222)
print(Decimal(0.12341)*222222)


import math
testnumber=round(math.pi,3)
print(testnumber)

print(divmod(147,25))   #获得商和余数

#有理数
from fractions import Fraction
num_1=Fraction(12,18)   #分子和分母
print(num_1)
num_2=Fraction(0.431254)
print(num_2)



"""


#math 模块
import math 
print(math.pi,math.e,math.ceil(432.53425),math.floar(432.53425))

print(math.exp(5))  #计算e的多少次
"""
sqrt()计算平方根
pow(x,y)计算x的y次
fomd(x,y)计算x%y的余数
hypot(x,y)计算x,y方之和 并开平方
gcd(x,y)计算x,y的最大公约数n
"""