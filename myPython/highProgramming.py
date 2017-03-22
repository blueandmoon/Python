from types import MethodType
from enum import Enum
from enum import Enum, unique
from helly import Hello


print('------------------------------分割线---------------------------__slots__------------------------------------------')

class Student(object):
    pass

s = Student()
s.name = 'Michael'  #   动态给实例绑定一个属性
print(s.name)

def set_age(self, age): #   定义一个函数作为实例方法
    self.age = age

s.set_age = MethodType(set_age, s)  #   给实例绑定一个方法
s.set_age(23)   #   调用实例方法
print(s.age)

#   给一个实例绑定的方法, 对另一个实例是不起作用的
s2 = Student()
# s2.set_age(24)    #   无法调用

#   为了给一个类的所有实例都绑定方法, 可以给class绑定方法:
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s2.set_score(100)
print(s2.score)
s.set_score(88)
print(s.score)


#   如果我们想要限制实例的属性, 比如, 只允许对Student实例添加name和age属性, 我们可以在定义class的时候, 定义一个特殊的__slots__变量, 来
#   限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') #   用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 33
# s.score = 99    #   会出错

#   注意: __slots__定义的属性仅对当前类实例起作用, 对继承的子类是不起作用的

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 88

print(g.score)

#   除非在子类中也定影__slots__, 这样, 子类实例允许定义的属性就是自身的__slots__加上父类的__


print('-----------------------------------分割线---------------------------------@property-------------------------------')


#   使用set_name() 和get_name()方法来赋值可以检查参数
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise  ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(89)
print(s.get_score())

# s.set_score(101)    #   会报错
#   Python内置的@property装饰器可以把一个方法变成属性调用
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 70
print(s.score)

# s.score = 111

#   还可以定义只读属性, 只定义getter方法, 不定义setter方法就是一个只读属性
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth
#   这里, birth是读写属性, age是只读属性

s = Student()
s.birth = 1992
print(s.birth, s.age)


#   练习: 利用@property给一个Screen对象加上一个width和height属性, 已经一个只读属性resolution
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 30
s.height = 60

print(s.resolution)

print('-------------------------------------分割线--------------------------多重继承--------------------------------------')

#   通过多重继承, 一个子类可以获得多个父类的所有功能, 这种设计通常称为MixIn

class Animal(object):
    pass

#   大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#   各种动物
class Dog(Mammal):
    pass

class Bat(Animal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

#   多重继承优先继承第一个父类(在父类名方法重复时), 第一个继承是生父, 后边都是继父, 优先继承生父的

print('-----------------------------------分割线--------------------------------定制类------------------------------------')

class Student(object):
    def __init__(self, name):
        self.name = name

        def __str__(self):
            return 'Student object (name: %s)' % self.name

        __repr__ = __str__

print(Student('Michael'))

#   定义好__str__()方法, 就可以修改返回打印的字符串了...怎么没有用

#   __iter__    如果一个类想要被用于for...in循环, 类似list或tuple那样, 就必须实现一个__iter__方法, 该方法返回一个迭代对象, 然后,
#   Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值, 直到遇到StopIteration错误时退出循环

#   以斐波那契数列为例, 写一个Fib类, 可以作用于for循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1   #   初始化两个计数器a, b

    def __iter__(self):
        return self #   实例本身就是迭代对象, 故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b    #   计算下一个值
        if self.a > 1000:   #   退出循环的条件
            raise  StopIteration()
        return self.a   #   返回下一个值

for n in Fib():
    print(n)


#   __getitem__ 要想像list那样使用下标获取元素, 需要实现__getitem__()方法:
class Fib(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

f = Fib()
print(f[7])

#   list有个神奇的切片方法
print(list(range(100))[5:10])

#   对于Fib却报错, 原因是__getitem__传入的参数可能是一个int, 也可能是一个切片对象slice, so, 要做判断:
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):   #   item是索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a

        if isinstance(item, slice): #   item是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                    a, b = b, a + b
            return L

f = Fib()
print(f[0:10])  #   但是没有对step参数和负数做处理, 并不完善

#   __getattr__ 正常情况下, 当我们调用类的方法或者属性时, 如果不存在, 就会报错, 比如:
class Student(object):
    def __init__(self):
        self.name = 'Michael'

s = Student()
print(s.name)

# print(s.score)    #   会报错, 要想避免这个错误, 可以写一个__getattr__方法, 动态返回一个属性, 如下
class Student(object):
    def __init__(self):
        self.name = 'Allen'

    def __getattr__(self, item):
        if item == 'score':
            return 99

s = Student()
print(s.score)

#   返回函数也可以, __getattr__方法只有在没找到属性的情况下才会调用, 已存在的不会调用
class Student(object):

    def __getattr__(self, item):
        if item == 'age':
            return lambda :25
#   只是调用方式变为:
s = Student()
print(s.age())

# print(s.abc)    #   这是因为我们定义的__getattr__默认返回的就是None
#   要让class只响应特定的几个属性, 我们要按照约定, 抛出AttributeError的错误:
class Student(object):

    def __getattr__(self, item):
        if item == 'age':
            return 23
        else:
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

s = Student()
# print(s.a)

#   这实际上可以把一个类的所有属性和方法调用全部动态化处理了, 不需要任何特殊手段, 作用是可以针对完全动态的情况做调用

#   利用完全动态的__getattr__, 我们可以写出一个链式调用:
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

#TODO   - 不明觉厉, 很厉害的样子, 重点!^

#   __call__    一个对象实例可以有自己的属性和方法, 当我们调用实例方法时, 我们用instance.method()来调用. 能不能直接在实例本身上调用呢, 可以!
#   只要定义一个__call__()方法, 就可以直接对实例进行调用, 如下
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)

s = Student('Ajax')
print(s())

#   __call__()还可以定义参数. 对实例进行直接调用就好比对一个函数进行调用一样, 所以完全可以吧对象看成函数, 把函数看成对象, 两者没有根本区别
#   如果把对象看成函数, 那么函数本身其实也可以在运行期间动态创建出来, 因为类的实例都是运行期创建出来的, 这么一来, 我们就模糊了对象和函数的界限
#   判断一个变量是对象还是函数, 我们需要判断一个对象能否被调用, 能被调用的对象就是一个Callable对象, 比如函数和上面定义的带有__call__()d类实例
print(callable(s))
print(callable(max))
print(callable('abc'))
print(callable(None))
print(callable([1, 2, 3]))


print('-----------------------------------------分割线---------------------------枚举类----------------------------------')

#   当我们需要定义常量时, 一个办法是用大写变量通过证书来定义, 例如月份:
JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12
print(JAN, NOV) #   好处是简单, 缺点是类型是int, 并且仍然是变量

#   更好的方法是为这样的枚举类型定义一个class类型, 然后每个常量都是class的一个唯一实例
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

#   value属性是自动赋给成员的int常量, 默认从1开始计数
print(Month.May.name, Month.May.value)

#   如果需要更精确地控制枚举类型, 可以从Enum派生出自定义类 from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 #   Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#   @unique装饰器可以帮我们检查保证没有重复值
print(Weekday.Mon)
print(Weekday.Tue.value)
print(Weekday(3))
# print(Weekday(7))

print('-------------------------------------分割线--------------------------元类-----------------------------------------')

#   动态语言和静态语言最大的不同, 就是函数和类的定义, 不是在编译时定义的, 而是运行时动态创建的
h = Hello()
print(h.helllo())
print(type(Hello))
print(type(h))  #   type()函数可以查看一个类型或者变量的类型, Hello是一个class, 它的类型就是type, 而h是一个实例, 它的类型就是class Hello
#   我们说class的定义是运行时动态创建的, 而创建class的方法就是使用type()函数
#   type()函数既可以返回一个对象的类型, 也可以创建出新的类型, 比如, 我们可以通过type()函数创建出Hello类, 而无需通过class Hello(object)...的定义

def fn(self, name='world'): #   先定义函数
    print('Hello, new %s' % name)

Hello = type('Hello', (object,), dict(hell=fn))   #   创建Hello class

h = Hello()
print(h.hell())

#   要创建一个class对象, type()函数依次传入3个参数:
#       1. class的名称
#       2. 继承的父类集合, 主要Python支持多重继承, 如果只有一个父类, 别忘了tuple的单元素写法
#       3. class的方法名称与函数绑定, 这里我们把fn绑定到方法名hello上


#   TODO    - metaclass

#   除了使用type()动态创建类之外, 要控制类的创建行为, 还可以使用metaclass
#   先定义metaclass, 就可以穿件类, 最后创建实例

#   eg: 给我们自定义的MyList增加一个add方法
#   定义ListMetaclass, 按照默认习惯, metaclass的类名总是以Metaclass结尾, 以便清楚地表示这是一个metaclass:
#   metaclass是类的模板, 所以必须从'type'类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

#   有了ListMetaclass, 我们在定义类的时候还要指示使用ListMetaclass来定制类, 传入关键字参数metaclass:
class MyList(list, metaclass=ListMetaclass):
    pass

#   当我们传入关键字参数metaclass时, 魔术就生效了, 它指示Python解释器在创建MyList时, 要通过ListMetaclass.__new__()来创建, 在此
#   我们可以修改类的定义, 比如, 加上新的方法, 然后, 返回修改后的定义

#   __new__()方法接收到的参数依次是:
#       1. 当前创建的类的对象
#       2. 类的名字
#       3. 类继承的父类集合
#       4. 类的方法集合

L = MyList()
L.add(1)
print(L)
#TODO   自定义函数加上呢?

#   而普通的list没有add方法
L2 = list()
# L2.add(1)

print('-------')

#TODO   - 使用 元类修改类定义: ORM是个典型例子
#   ORM全称'Object Relational Mapping', 即对象-关系映射, 就是把关系数据库的一行映射为一个对象, 也就是一个类对应一个表, 这样, 写代码更简单
#   不用直接操作SQL语句
#   要编写一个ORM框架, 所有的类都只能动态定义, 因为只有使用者才能根据表的结构定义出对应的类来.
#   let me create a ORM framework
#   编写底层模块的第一步, 就是先把调用接口写出来, 比如, 使用者如果使用这个ORM框架, 想定义一个User类来操作对应的数据库表User, 我们期待他
#   写出这样的代码:

# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# # 创建一个实例：
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# # 保存到数据库：
# u.save()

#   其中, 父类Model和属性StringField, IntegerField是由ORM框架提供的, 剩下的魔术方法比如save()全部由metaclass自动完成, 虽然metaclass
#   的编写会比较复杂, 但是ORM的使用起来却异常简单

#   现在按照上面的接口来实现该ORM
#   首先定义Field类, 它负责保存数据库表的字段名和字段类型:
class Field(object):
    def __init__(self, name, clumn_type):
        self.name = name
        self.clumn_type = clumn_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

#   在Field的基础上, 进一步定义各种类型的Field, 比如StringField, IntegerField等等:
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

#   下一步, 就是编写最复杂的ModelMetaclass了:
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings    #   保存属性和列的映射关系
        attrs['__table__'] = name   #   假设表明和类名一致
        return  type.__new__(cls, name, bases, attrs)

#   以及基类Model:
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

#   当用户定义一个class User(Model)时, Python解释器首先在当前类User的定义中查找metaclass, 如果没找到, 就继续在父类Model中查找metaclass,
#   找到了, 就使用Model中定义的metaclass的ModelMetaclass来创建User类, 也就是说, metaclass可以隐式的集成到子类, 但是子类自己却感觉不到.

#   在ModelMetaclass中, 一共做了几件事情:
#   1. 排除掉对Model类的修改;
#   2. 在当前类(比如user)中查找定义的类的所有属性, 如果找到一个Field属性, 就把它保存到一个__mappings__的dict中, 同事从类属性中删除该Field属性
#       , 否则, 容易造成运行时错误(实例的属性会遮盖掉类的同名属性);
#   3. 把保存到__table__中, 这里简化为表名默认为类名

#   在Model类中, 就可以定义各种操作数据库的方法, 比如save(), delete, find(), update等等.
#   我们实现了save()方法, 把一个实例保存到数据库中. 因为有表名, 属性到字段的映射和属性值的集合, 就可以构造出INSERT语句.

#   编写代码试试:
class User(Model):
    #   定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

#   创建一个实例:
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
#   保存到数据库:
u.save()

#   可以看到, save()方法已经打印出了可执行的SQL语句, 以及参数列表, 只需要真正连接到数据库, 执行该SQL语句, 就可以完成真正的功能
#   so, 通过metaclass, 不到100行代码实现了一个精简的ORM框架

age = 34
print(age.__class__)
print(age.__class__.__class__)

#   TODO    - 自定义元类
#   TODO    - 这个例子更好懂
#   元类会自动将你通常传给'type'的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    #   返回一个类对象, 将属性都转为大写形式
    #   选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

    #   将他们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    #   通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)

# __metaclass__ = upper_attr  #   这会作用到这个模块中的所有类

class Foo(object, metaclass=upper_attr):
    #   我们也可以在这里定义__metaclass__, 这样就只会作用到这个类中
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

#   TODO    再一个
#   type实际上是一个类, 就像str和int一样
class UpperAttrMetaClass(type):
    #   __new__是在__init__之前被调用的特殊方法
    #   __new__是用来创建对象并返回之的方法
    #   而__init__只是用来将传入的参数初始化给对象
    #   一般很少用到__new__, 除非你希望能够控制对象的创建
    #   这里, 创建的对象是类, 我们希望自定义它, 所以, 在这里改写__new__
    #   如果你希望的话, 也可以在__init__中做些事情
    #   还有一些高级的用法会涉及到改写__call__特殊方法, 但是在这不用
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attrs):
        attrs = ((name, value) for name, value in future_class_attrs.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return  type(future_class_name, future_class_parents, uppercase_attr)

class Foo1(object, metaclass=UpperAttrMetaClass):
    zip = 'zip'

print('---')
print(hasattr(Foo1, 'zip'))
print(hasattr(Foo1, 'ZIP'))

#   但是, 这种方式其实不是OOP. 我们直接调用了type, 而且我们没有改写父类的__new__方法, 改写之:
class UpperAttrMetaClass(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        #   复用type.__new__方法
        #   这就是基本的OOP编程, 没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)

class Foo2(object, metaclass=UpperAttrMetaClass):
    foo = 'foo'

print('-------')
print(hasattr(Foo2, 'foo'))
print(hasattr(Foo2, 'FOO'))

#   注意, 上面有个额外的参数upperattr_metaclass, 这是因为类方法的第一个参数总是表示当前的实例, 就像在普通方法中的self一样,
#   一次在真实的产品代码中一个元类应该是这样的:
class UpperAttrMetaClass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls, name, bases, uppercase_attr)

#   如果用super方法的话, 还可以使它更清晰一些, 这会缓解集成(是的, 你可以拥有元类, 从元类集成, 从type继承)
class UpperAttrMetaClass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaClass, cls).__new__(cls, name, bases, uppercase_attr)

class Foo3(object, metaclass=UpperAttrMetaClass):
    zxy = 'zyx'

print('---3--')
print(hasattr(Foo3, 'zxy'))
print(hasattr(Foo3, 'ZXY'))

#   元类的本质:
#   1. 拦截类的创建
#   2. 修改类
#   3. 返回修改之后的类








































