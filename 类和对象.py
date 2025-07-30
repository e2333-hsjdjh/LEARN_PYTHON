#类的定义

class Animal:
#函数在类里面叫方法
#变量叫属性
    name=None
    age=None
    species=None
    sound=None
    diet=None
    health_status=None
    eat_time_everyday=None


    def make_sound(self):
        return f"{self.name} makes a sound: {self.sound}"
    
    def age_in_human_years(self):
        return self.age * 7
    
dog= Animal()
dog.name = "Buddy"
dog.age = 5 
dog.species = "Dog"
dog.sound = "Woof"
dog.diet = "Carnivore"
dog.health_status = "Healthy"
dog.eat_time_everyday = "8:00 AM, 6:00 PM"

print(dog.make_sound())
print(f"{dog.name} is {dog.age_in_human_years()} years old in human years.")


#pig= Animal(name="Porky", age=3, species="Pig", sound="Oink", diet="Omnivore", health_status="Healthy", eat_time_everyday="7:00 AM, 5:00 PM")


class Animal_2:
    #类内要写self，但是类外不需要写self
    #self代表类的实例化对象
    def __init__(self, name, age, species, sound, diet, eat_time_everyday, health_status='health'):
        self.name = name
        self.age = age
        self.species = species
        self.sound = sound
        self.diet = diet
        self.health_status = health_status
        self.eat_time_everyday = eat_time_everyday

    def make_sound(self):
        return f"{self.name} makes a sound: {self.sound}"
    
    def age_in_human_years(self):
        return self.age * 7
    
dog_2 = Animal_2("Buddy", 5, "Dog", "Woof", "Carnivore", "8:00 AM, 6:00 PM", "Healthy")
print(dog_2.make_sound())
print(f"{dog_2.name} is {dog_2.age_in_human_years()} years old in human years.")
cat_2=Animal_2(name="Whiskers", age=4, species="Cat", sound="Meow", diet="Carnivore", health_status="Healthy", eat_time_everyday="7:30 AM, 5:30 PM")

print()
print(cat_2)
print()




#魔术方法
class Animal_3:
    def __init__(self, name, age, species, sound, diet, eat_time_everyday, health_status='healthy'):
        self.name = name
        self.age = age
        self.species = species
        self.sound = sound
        self.diet = diet
        self.health_status = health_status
        self.eat_time_everyday = eat_time_everyday

    def __str__(self):
        return f"{self.name} is a {self.species} aged {self.age} years."

    def __repr__(self):
        return f"Animal_3(name={self.name}, age={self.age}, species={self.species})"
    
    def __add__(self, other):
        if isinstance(other, Animal_3):
            return self.age + other.age
        return NotImplemented
    
    def __sub__ (self, other):
        if isinstance(other, Animal_3):
            return self.age - other.age
        return NotImplemented
    def __call__(self):     #将一个类转变为一个可调用对象
        print( f"{self.name} is a {self.species} that says {self.sound} and eats {self.diet}.")


cat_3 = Animal_3("Whiskers", 4, "Cat", "Meow", "Carnivore", "7:30 AM, 5:30 PM", "Healthy")
print(cat_3)                        # 调用 __str__ 方法
print(repr(cat_3))                  # 调用 __repr__ 方法
dog_3 = Animal_3("Buddy", 5, "Dog", "Woof", "Carnivore", "8:00 AM, 6:00 PM", "Healthy")
print(callable(cat_3))
cat_3()                             #调用__call__()方法


print(cat_3 + dog_3)                # 调用 __add__ 方法，输出年龄之和
print()
print()
print()
print()

class Person:
    
    #1   __init__

    def __init__(self):
        print("这里是__init__方法")
        print(self)

    #    __new__
    #原先是调用内存
    #现在不加super则只是覆盖而不能调用其他的

    def __new__(cls,*args,**kwargs):  #cls代表类本身
        print("我是__new__")
        print(cls)
        res=super().__new__(cls)  #方法重写，res里面保存的是实例化对象的引用
        #__new__是静态方法，实参必须传cls
        #注意重写__new__时一定要写return否则得不到相应的引用，则不会调用
        return res
#实例化对象的过程:
#首先执行__new__(),返回一个实例对象
#再去调用__init__,d对对象进行初始化
pe=Person()
print(pe)



#单例模式:
#可以理解为一个特殊的类，他只有一个实例化对象
#优点:可以节省内存空间，减少不必要的资源浪费
#缺点:多线程访问时容易引发线程安全问题

#1.通过@classmethod实现
#2.通过装饰器实现



#3.重写__new__方法；

class A:
    pass
a1= A()
a2=A()
print(a1)
print(a2)
    #实现单例模式，对象的地址一样
    #1.定义一个类属性，用于记录单例对象的引用
    #2.重写__new__()方法
    #3.判断，
    #4.返回类属性中对象的引用
print()
print()
class A:
    obj=None
    def __new__(cls,*arge,**kwargs):
        print("这是__new__()方法")
        if cls.obj==None:
            cls.obj=super().__new__(cls)
        return cls.obj
    def __init__(self):
        print("我是__init__()")
s=A()
print(s)
s1=A()
print(s1)

#4.通过导入文件完成：
import progressbar as sss
import progressbar as ss
print(id(sss))
print(id(ss))

#应用场景:
#回收站对象
#音乐播放器
#开发游戏软件
#数据库搭建







#魔法方法/属性:
class m:
    """人类"""
    #__module__():表示当前操作对象所在模块
    #__doc__类的描述信息
print(m.__doc__)


print()
print()

dog_3()

print()
print()
print()



#类的封装：私有属性与公有属性


class animal_4:
    __name_sjai='dsgafad'
    pair=None
    def __init__(self,pair):
        self.pair=pair
    def get_name(self):
        return self.__name_sjai
a=animal_4(1)
#print(a.__name_sjai)

print(a.get_name())


#类的继承：
class aniaml_5(animal_4):
    age=321
    def __init__(self,pair):
        super().__init__(pair)



b=aniaml_5('无')
b.age=23
print(b.age)
print(b.get_name())
print(b.pair)
    
#如果子类重新写一个一样的，那么原先的就会被覆写

#也可以继承多个类



#析构函数:
class person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} has been created.")

    def __del__(self):
        print(f"{self.name} is being deleted.")

p = person("Alice")
print(p.name)  # 输出: Alice
#最后代码结束时会销毁自动调用__del__
#或者运用del p



class Person:
    name='小明'   #类属性:类所拥有的属性

    def __init__(self,age):
        self.age=age

    def play(self):
        print(f"{Person.name}在玩游戏")
        print(self.name)

    @staticmethod
    def into():
        print(f"我是{Person.name}")

    @classmethod
    def into_2(cls):
        print(cls.name)
        try:
            print(self.name)
        except NameError as e:
            print(f"{e}无法访问self")
pe=Person(10)
pe.play()

print()
print()
pe.into_2()





