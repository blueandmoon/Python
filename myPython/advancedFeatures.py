from collections import Iterable
from  collections import Iterator
from functools import reduce
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
def prod(L):
    









































































































































































































































































