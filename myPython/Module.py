from helly import test
from  helly import greeting
from PIL import Image
import types
import sys

print('-------------------------------分割线-------------------------模块---------------------------------')

test()

#   作用域
#   正常的函数和变量名是公开的, 可以被直接饮用, 比如: abc, x123, PI等
#   类似__xxx__这样的变量是特殊变量, 可以被直接引用, 但是有特殊用处, 比如__author__, __name__
#   类似_xxx和__xxx这样的函数和变量名是非公开的private, "不应该"(Python并没有方法可以完全限制访问private函数或变量)被直接引用, 比如_abc, __abc等

print(greeting('打个招呼'))

#   第三方模块Pillow, 安装命令: pip3 install Pillow
im = Image.open('img/2.png')
print(im.format, im.size, im.mode)
im.thumbnail((203.5, 100))
im.save('thumb.jpg', 'JPEG')

#   生出了缩略图
im2 = Image.open('thumb.jpg')
print(im2.format, im2.size, im2.mode)

#   当我们要加载一个模块时, Python会在指定的路径下搜索对应的.py文件,找不到会报错
#   默认情况下, Python解释器会搜索当前目录, 所有已安装的内置模块和第三方模块, 搜索路径存放在sys模块和path变量中
print(sys.path)

#   如果要添加自己的搜索目录, 两种方法: 1. 直接修改sys.path, 添加要搜索的目录"
# sys.path.append('/Users/Ligen/hhh')
#   这种方法在运行时修改, 运行结束后失效

#   第二种方法是设置环境变量PYTHONPATH, 改环境变量的内容会被自动添加到模块搜索路径中, 设置方式和设置Path环境变量类似

print('------------------------------分割线----------------------------类和实例---------------------------------------')

class Student(object):
    pass

bart = Student()
print(bart)
print(Student)

#   可以自由给一个实例绑定属性
bart.name = 'Bart Simpson'
print(bart.name)

#   在创建实例的时候, 可以把我们认为必须绑定的属性强制填写进去, 通过定义一个特殊的__init__方法, 在创建实例的时候, 把name, score等属性绑上去
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

#   __init__方法的第一个参数永远是self, 表示创建的实例本身, 有了__init__方法, 创建的时候就不能传入空参数了
bart = Student(name='Ajax', score=33)
bart.te = 'hehe'
print(bart.name, bart.score, bart.te)

#   和普通函数相比, 在类中定义的函数只有一点不同, 就是第一个参数永远是实例变量self, 只不过在调用时, 不用传递该参数. 除此之外, 没有区别

def print_score(std):
    print('__%s: %s' % (std.name, std.score))

print_score(bart)


#   在类内部定义的方法叫做类方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s_:_%s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student(name='Allen', score=88)
bart.print_score()

print(bart.get_grade())

#   类是创建实例的模板, 而实例则是一个一个具体的对象, 各个实例的数据都互相独立, 互不影响;
#   方法就是与实例绑定的函数, 和普通函数不同, 方法可以直接访问实例的数据

print('---------------------------------分割线--------------------------访问限制----------------------------------------')

##  设置私有属性, 实例的变量名如果以__开头, 就是私有变量

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' %(self.__name, self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

bart = Student('Bart Simpson', 89)
# print(bart.name)

#   如果外界想要获取私有变量的值, 可以给类加上get_name,get_core这样的方法
print(bart.get_name())

#   想要在外界修改类的私有属性, 加上set_name,set_score这样的方法
#   双下划线的私有变量在外界可以用 _Student__name来访问, 如下

bart.set_score(33)
print(bart.get_score())

print(bart._Student__name)


print('-----------------------------------分割线---------------------------继承和多态-----------------------------------')

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
cat = Cat()

dog.run()
dog.eat()
cat.run()

#   子类和父类拥有相同的run()方法时, 子类会覆盖父类的方法, 在代码运行时, 总是会调用子类的同名方法

#   当我们定义一个class的时候, 其实就是定义了一种数据类型
a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))

print(isinstance(c, Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

run_twice(Dog())


#   对于静态语言(例如Java)来说, 如果需要传入Animal类型, 则传入的对象必须是Animal类型或者它的子类, 否则, 将无法调用run()方法
#   对于Python这样的动态语言来说, 不一定需要传入Animal类型, 只需要保证传入的对象有一个run()方法就可以了

class Timer(object):
    def run(self):
        print('start...')
#   这就是动态语言的"鸭子类型"

print('-----------------------------分割线----------------------------获取对象信息-----------------------------------')

#   判断对象类型, 使用type()方法
print(type(122))
print(type('333'))
print(type(c))

#   判断一个对象是否是函数, 如下:
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)


#   使用isinstance也可以判断
print(isinstance([1, 2, 3], (list, tuple)))

#   如果要获取一个对象的所有属性和方法, 可以使用dir()方法, 它返回一个包含字符串的list
print(dir('abc'))

#   类似__xxx__的属性和方法在Python中都是有特殊用途的, 比如__len__方法返回长度, 比如获取一个对象的长度 调用len(), 在函数内部, 它会
#   自动调用该对象的__len__()方法, so, 下面的代码是等价的:
print(len('abc'))
print('abc'.__len__())

#   如果自己写的类, 也想要使用len(myObj)的话, 可以自己写个__len__方法:
class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

print('ABV'.lower())

#   配合getattr(), setattr(), hasattr(), 可以操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(obj.x)

print(hasattr(obj, 'x'))

print(hasattr(obj, 'y'))

setattr(obj, 'y', 77)

print(hasattr(obj, 'y'))

print(getattr(obj, 'y', '404')) #   404是默认值, 自己设定

print(obj.y)

#   也可以获取对象的方法
print(hasattr(obj, 'power'))

print(getattr(obj, 'power'))

fn = getattr(obj, 'power')

print(fn()) #   调用fn()和调用obj.power()是一样的


print('---------------------------------分割线------------------------------实例属性和雷属性-------------------------------')

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

#   为一个类本身绑定一个属性, 为类属性
class Student(object):
    name = 'Student'

s = Student()   #   创建实例
print(s.name)

print(Student.name)

s.name = 'Michael'
print(s.name)
print(Student.name)

del s.name
print(s.name)

#   so, 不要把实例属性和类属性使用相同的名字, 因为相同名称的实例属性将屏蔽掉类属性, 但是当你删除掉实例属性后, 再使用相同的名称,
#   访问到的将是类属性



























































































