from collections import Iterable
from  collections import Iterator
from functools import reduce
import functools
import os

#   高级特性
print('---------------万恶的--------------分割线----------------切片-------------------')

L= ['Michael', 'Sarach', 'Tracy', 'Bob', 'Jack']

#   切片操作, L[0:3]: 表示从0索引开始, 到索引3位置, 如果起始索引为0, 可省略   [fromIndex:toIndex:step]
print(L[:3])
print(L[-1])
print(L[2:3])
#   同样可以倒着切片, 最后一个索引为-1
print(L[-2:])
print(L[-2:-1])


L = list(range(100))
print(L[:10])
print(L[-10:])
print(L[10:20])
#   前10个数, 每两个取一个
print(L[:10:2])
#   所有数, 每五个取一个
print(L[::5])
print(L[:])

#   tuple也是一种list, 只是不可变, 因此tuple也可以进行切片操作, 操作结果仍然是tuple
t = tuple(range(100))
print(t[::3])

#   字符串 'xxx' 也可以看做一种list, 每个元素就是一个字符, 也可以进行切片操作, 返回结果仍是字符串
s = 'Hello world!'
print(s[:2])
print(s[::2])


print('-------------------------分割线------------------------迭代--------------------------------')
#   通过for循环遍历一个list或者tuple, 称为迭代(Iteration)     for ... in
#   只要是可迭代对象, 都可迭代, 比如说dict, dict无序, 迭代的结果也是无序的, 字符串也可以迭代
d = {'a': 1, 'b': 2, 'c': 5}
for key in d:
    print(key, d[key])

for ch in '迭代☺':
    print(ch)

#   判断是否是可迭代对象: 通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


print('------------------------分割线-----------------------列表生成式-----------------------------------')
#   列表生成式即List Comprehensions, 是Python内置的非常强大的用来创建list的生成式
L = list(range(3, 11))
print(L)

#   生成[1*1, 2*2, 3*3, ..., 10*10]
L = [x * x for x in range(1, 11)]
print(L)
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

#   生成全排列
print([m + n for m in 'abc' for n in 'xyz'])

#   获取当前目录下的所有文件和目录名
print(os.listdir(os.getcwd()))
g = [d for d in os.listdir('/Users/apple/ligen/Python/myPython')]
print(g)

#   批量处理字符串
L = ['Hello', 'World', 'IBM', 'YaHoo']
print([s.lower() for s in L])

#   加过滤条件
L= ['Hello', 'World', 12, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])


print('-----------------------------------------分割线---------------生成器 generator--------------------------------------')

#   一边循环一边计算的机制叫做生成器generator
#   第一中方式很简单, 把列表生成式的[]改成(), 就创建了一个generator, 通过next()方法获取generator的下一个返回值
L = (x * x for x in range(10))
print(next(L))
print(next(L))
print(next(L))
print(next(L))

#   斐波那契数列Fibonacci 1, 1, 2, 3, 5, 8, 13, ...
def fib(max):
    print('start')
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        #   注意复制语句
        a, b = b, a + b
        n += 1
    print('done')
fib(7)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
f = fib(6)
print(next(f))
print(next(f))
print(next(f))
print(f)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o = odd()
print(next(o))
print(next(o))
print(next(o))

#   generator的执行流程和函数不一样, 函数是顺序执行, 遇到return或者最后一句函数语句就返回, 而在generator的函数中, 每次调用next()的时候
#   执行, 遇到yield语句返回, 再次执行的时候从上次返回的yield语句处继续执行

for n in fib(6):
    print(n)

#   使用for循环调用generator时, 发现拿不到generator的return的返回值, 想要拿到generator的返回值, 必须捕获StopIteration错误, 返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

#   杨辉三角~~~
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

L = triangles()
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))


print('----------------------------------分割线--------------------------迭代器-------------------------------------')

#   可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator;    可以使用isinstance()来判断一个对象是否是Iterator是否是一个Iterator对象
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))


print('-----------------------------------分割线------------------------函数式编程-Higher-order function---------------------------------------')

f = abs
print(f)
#   变量可以指向函数, 函数名就是变量
print(f(-5))

# abs = 10
# print(abs(-8))

#   一个函数可以接受另一个函数作为参数, 这种函数成为高阶函数, eg:
def add(x, y, z):
    return z(x) + z(y)

print(add(-3, -5, abs))

#   map/reduce
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7])
print(list(r))

r = map(abs, [-1, 3, -5, 8, 9])
print(list(r))

r = map(str, [-1, 3, 8, 9, 0])
print(list(r))


#   reduce把一个函数作用于一个序列[x1, x2, x3, ...]上, 这个函数必须接收两个参数, reduce把结果继续和序列的下一个元素做累积运算

#
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 7, 2]))

#   TODO   - 这个鬼东西每次传入一个char字符, 转化为int输出
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}[s]

r = char2num('3')
print(r)

print(reduce(fn, map(char2num, '77890')))

#   再次整理一下就是
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}[s]
    return reduce(fn, map(char2num, s))

print(str2int('789'))

#   还可以用lambda函数进一步简化为:
def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}[s]
def str2int(s):
    return reduce(lambda  x, y: x * 10 + y, map(char2num, s))

print(str2int('239'))


#   TODO    - 练习
#   1. 利用map()函数, 把用户输入的不规范的英文名字, 变为首字母大写, 其他小写的规范名字, 输入['adam', 'LISA', 'barT']
#      输出['Adam', 'Lisa', 'Bart']:

def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#   Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def multi(x, y):
    return x * y
def prod(List):
    return reduce(multi, List)

print(prod([2, 3, 6]))


#   利用map和reduce编写一个str2float函数, 吧字符串'123.456'转换为浮点数123.456

def str2float(s):
    def mul(x, y):
        return 10 * x + y
    def trans(chr):
        return {'0': 0, '1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[chr]
    def power(n):
        c = 1
        while n:
            c *= 10
            n -= 1
        return c
    for i, j in enumerate(s):
        if j == '.':
            c = i
            break
    rx = reduce(mul, map(trans, s[:c]))
    ry = reduce(mul, map(trans, s[c+1:len(s)]))
    return rx + ry/power(len(s) -c -1)
print(str2float('224.567'))


print('-------------------------------------------分割线---------------------------------filter--------------------------------------------')

#   filter: 过滤器, 接受一个函数和一个序列, filter()把传入的函数依次作用于每个元素, 然后根据返回值是True还是False决定保留还是丢弃该元素

#   删除偶数, 保留奇数
def is_odd(n):
    return n % 2 == 1
L = filter(is_odd, [1, 2, 3, 4, 5, 6, 7])
print(L)
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))

#   删除空字符
#   s.strip(rm): 删除s字符串的开头, 结尾处, 位于rm删除序列的字符
#   s.lstrip(rm): 删除s字符串位于开头处, 的rm字符
#   s.rstrip(rm): 删除s字符串结尾处, 的rm字符
def not_empty(s):
    return s and s.strip('6')
print(list(filter(not_empty, ['a', 'b', '', '6'])))


#   用filter求素数, 依次过滤掉2, 3, 5, ... 的倍数的自然数就是素数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda  x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 10:
        print(n)
    else:
        break


#   练习: 回数是指从左向右读和从右往左读都一样的数
def is_palindrome(n):
    return str(n) == str(n)[::-1]
r = filter(is_palindrome, range(1, 100))
print(list(r))

res = filter(lambda num: str(num) == str(num)[::-1], range(1, 1000))
print(list(res))

print('------------------------------------------分割线---------------------------sorted---------------------------------')

print(sorted([-1, 3, -7, 9, 2]))
print(sorted([-1, 3, -7, 9, 2], key=abs))


s = ['bob',  'about', 'Zoo', 'Credit']
print(sorted(s))
print(sorted(s, key=str.lower)) #  忽略大小写排序
print(sorted(s, key=str.lower, reverse=True))   #   反向传值

#   练习: 假设我们用一组tuple表示学生名字和成绩: L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_name)
print(L2)
print(sorted(L, key=by_score))

print('------------------------------------分割线-----------------------------返回函数------------------------------------')
#   通常求和函数的定义是这样的:
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax

print(calc_sum(2, 3, 8))

#   如果不立即求和, 想在后面的代码中根据需要再计算, 可以返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
f = lazy_sum(3, 22, 1)
print(f)
#   只有在调用f时, 才真正计算求和的结果:
print(f())

#   注意: 当我们调用lazy_sum() 时, 每次调用都返回一个新的函数, 即使传入相同的 参数
f1 = lazy_sum((2, 3, 4))
f2 = lazy_sum(2, 3, 4)
print(f1 == f2)

#   闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3()) #   全部是9, 原因就在于返回的函数引用了变量i, 但是它并非立刻执行, 等三个函数都返回时, 它们所引用的变量i已经都变成了3, 所以都是9
#   牢记: 返回函数不要一用任何循环变量, 或者后续会发生变化的变量

#   如果一定要引用循环变量, 方法就是再创建一个函数, 用该函数的参数绑定循环遍历当前的值, 无论改循环遍历后续如何更改, 已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) #   f[i]立刻被执行, 因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())

print(type(f1))

def best_count():
    return [(lambda  x: (lambda  :x * x)) (i) for i in range(1, 4)]
f1, f2, f3 = best_count()
print(f1(), f2(), f3())

#   匿名函数lambda
L= list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(L)

#   匿名函数也是一个函数对象, 也可以把匿名函数赋值给一个变量
f = lambda x: x * x
print(f)
print(f(5))

#   也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda :x * x + y * y
z = build(3, 6)

#   返回值是个lambda, 所以要执行才有值, z()
print(z())

print('-------------------------------------分割线------------------------装饰器----有点不太好懂-------------------------------------')

def now():
    print('2017-03-16')
f = now
f()

#  函数对象有个__name__s属性, 可以拿到函数的名字
print(f.__name__)

#   假设我们要增强now()函数的功能, 比如, 在函数调用前后自动打印日志, 但又不希望修改now()函数的定义, 这种在代码运行期间动态增加功能的方式, 称为"装饰器"(Decorator)
#   本质上, decorator是一个返回函数的高阶函数, so:
def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return  wrapper


# log(now())
# now()

now = log(now)
now()

#   如果decorator本身需要传入参数, 那就需要编写一个返回decorator的高阶函数 比如, 要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator
# @log('execute')
# def now():
#     print('2016.09.12')
# now()

now = log('hehehe')(now)
now()
#   经过修饰器修饰的函数, 其__name__已经变成了wrapper, 所以需要把原始函数的__name__等属性复制到wrapper()函数中, 否则, 有些依赖函数签名的代码执行就会出错
print(now.__name__)

#   so, 利用functools.wraps, 一个完整的decorator写法如下:
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('__call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

now = log(now)
now()

#   带参的decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

now = log('完整的decorator')(now)

now()

#   在面向对象(OOP)的设计模式中, decorator称为装饰模式


def test():
    print('测试之~')

test()

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(text + 'begin call %s():' % func.__name__)
            result = func(*args, **kwargs)
            print(text + 'end print')
            return result
        return wrapper
    print('end call' )
    if isinstance(text, str):
        return decorator
    else:
        f = text
        text = ''
        return decorator(f)
test = log('111')(test)
test()


print('-------------------------------------分割线----------------------------偏函数-------------------------------------')

#   使用int()把字符串转换为整数时, 还可以额外传入base参数, 默认为10, 可以做到N进制的转换
print(int('12345', 16))
print(int('11', base=2))

def int2(x, base=2):
    return int(x, base)
print(int2('10'))

int2 = functools.partial(int, base=2)
print(int2('11'))

#   so, functools.partial的作用就是, 把一个函数的某些参数给固定住(即设置默认值), 返回一个新的函数, 类似于OC中的继承
print(int2('111', base=10))


















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































