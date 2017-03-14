from abstest import my_abs
from  abstest import nop
import math

print('hello world!', '呵呵', 'can you tell me')

print('100 + 200 =', 100 + 200)

print('二十四桥明月在', '玉人何处教吹箫', '!')

# name = input("please input your name: ")
# print('hello, ', name)
#
# a = int(input("请输入一个数: "))
# if a >= 10:
#     print(a)
# else:
#     print(-a)

print(1.23e7)

print('I am "ok."')

#   r 可以表示引号内部的字符串默认不转义
print(r'\\\t\\')

# Python允许用'''...'''来表示多行内容
print('''...hhh
...222
666
yeah''')

#   布尔值, 有 and, or, not运算
print(3>2)
print(1 and 0)
print(1 or 0)
print('not运算符', '0 <-->', not 0,'1 <-->', not 1,'7 <-->', not 7)

#   空值, 空值在Python中是一个特殊的值, 用none表示, none不能理解为0, 因为0是有意义的, 而none是一个特殊的空值


print(10/3)
print(10//3)
print(10%3)

n = 123
f = 456.789
s1 = 'Hello world'
s2 = 'Hello \'Adam\''
s3 = r'Hello "Bart"'
s4 = r''''Hello,
Lisa!'''

print(n, f, s1, s2, s3, s4)

print('------------------------我是万恶的分割线------------------------------')

print('contains 中文')

# Python的字符串类型是str, 在内存中以Unicode表示, 一个字符对应若干个字节, 如果要在网络上传输, 或者要保存到磁盘上, 需要把str变为以字节为单位的bytes
# Python对bytes类型的数据用带b前缀的单引号或者双引号表示
x = b'ABC'
print(x)
#   注意: 'ABC' 和 b'ABC'不同, 前者是str, 后者虽然内容和前者一样, 但bytes的每个字符都只占用一个字节
# 以Unicode表示的str通过encode()方法可以编码为指定3的bytes
print('abc'.encode('ascii'))
print('中文'.encode('utf-8'))
#   中文无法编码为ascii编码, 会报错
# print('中文'.encode('ascii'))
#   在bytes中, 无法显示为ASCII字符的字节, 用 \x## 显示
#反过来, 从网络或者硬盘上读取了字节流, 那么读取到的数据就是bytes, 使用decode()方法把bytes转为str
print(b'ABC'.decode('ascii'), b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#   使用len()计算字符串的长度,
print(len('hello'))
print(len('中文'.encode('utf-8')))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

print('hello , %s' % 'hal')
# print('%d + %.2f' % (int(input()), 2.0))

a1 = 72
a2 = 87
a3 = (a2-a1)/a1
print(a3)

print('-----------------------------------万恶的----------分割----------线----------------------')

#   list类型
classmates = ['小兰', '小明', '小花']
print(classmates, len(classmates), classmates[1])
#   可以直接用-1 做索引, 直接获取最后一个元素, 倒数第二个是-2, 以此类推
print(classmates[-1], classmates[-2])

classmates.append('Adam')
print(classmates)

classmates.insert(2, 'Tracy')
print(classmates)

#   删除指定位置的元素, 用pop(i)
classmates.pop(2)
print(classmates)

classmates[2] = '花小'
print(classmates)

L = ['Apple', '种花家', 123, True]
print(L)

#   二维数组
p = ['asp', 'php', L]
print(p)

L= []
print(L, len(L))

#   tuple,  不可变的list
classmat = ('Michael', 'Bob', 'Tracy')
print(classmat)
classmat = ('a', 'B', 'c')

#   空的tuple
t = ()
print(t)
#   定义只有一个元素的tuple时, 必须加一个 ','  否则会产生歧义
t = (1)
print(t)
t = (1, )
print(t)

#   tuple只能保证指向不变, 其中包含list时, list中元素可变
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

print('------------------分------------割------------线------------------')

#   条件判断
#   根据Python的缩进原则, 缩进的语句视为代码块
age = 3
if age >= 20:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#   x不为空就为真, 为空就是false
x = 3
if x:
    print('True')


# birth = input('birth: ')
# if int(birth) < 2000:
#     print('00前')
# else:
#     print('00后')

# height = float(input('请输入身高(m): '))
# weight = float(input('请输入体重(kg): '))
# bmi = weight/(height * height)
# if bmi < 18.5:
#     print('太轻')
# elif 18.5 <= bmi < 25:
#     print('正常')
# elif 25 <= bmi < 28:
#     print('过重')
# elif 28 <= bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')


print('-------------万恶-----的--------------分割线-----------------------')
names = ['Pitter', 'Michael', 'Tracy']
for name in names:
    print(name)


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum += x
print(sum)

sum = 0
for x in range(101):
    sum += x
print(sum)


sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in range(len(L)):
    if x == 1:
        continue
    print(L[x])
print('END')


print('--------------------------分割线-------------------------------')

d = {'Michael': 96, 'Bob': 75, 'Allen': 88}
print(d, '\n', d['Allen'])

#   多次对一个key值赋值, 会把前次的值覆盖掉, key不存在会报错, 1. 通过in判断key值是否存在  2, 通过get方法, key不存在返回none, 或者自己制定的value
print('ddd' in d, d.get('aa', '无有'))

#   删除一个key, 用pop(key)方法
d.pop('Allen')
print(d)


# dict优缺点: 1. 查找和插入速度极快, 不会随着key增加而变慢, 2. 需要占用大量内存, 内存浪费多;  list与dict相反,




#   set和dict类似, 也是一组key的集合, 但不存储value;  要创建一个set, 需要提供一个list座位输入集合, 无序的
s = set([8, 2, -3])
print(s)

#   通过add(key)方法添加元素, Remove(key)来删除元素
s.add('5')
print(s)

s.remove('5')
print(s)


#   str不可变          a是变量, 'abc'才是字符串对象
a = 'abc'
b = a.replace('a', 'A')
print(a, b)


print('-----------------------------------分割线------------函数---------------------------')
#   https://docs.python.org/3/library/functions.html#abs
t = (2, '')
print(t)
print(all(t), any(t))

help(abs)
print(abs(-3))

print(max(2, 3, 1, 9))
print(max(s))
print(min(s))

print(int('223'))
print(bool(8), bool(-2), bool(0))
print(str(288))

help(hex)
print(hex(11))

#   自定义函数



print('自定义的绝对值函数', my_abs(-8))
# print('报错', my_abs('3'))
nop()

#   多返回值函数返回的实质上是一个tuple, 多个变量可以同时接收一个tuple, 按位置赋给对应的值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print(move(100, 100, 60, math.pi/6))


a, b = (3, 5)
print(a, b)

#   1, 定义函数时, 需要确定函数名和参数个数;
#   2, 如果有必要, 可以先对参数的数据类型进行检查
#   3, 函数体内部用return返回结果
#   4, 函数可以返回多个值, 实质上就是一个tuple


def quadratic(a, b, c):
    for z in  (a, b, c):
        if not isinstance(z, (int, float)):
            raise TypeError("Type Error !, %s" %(str(z)))
    # if not isinstance((a, b, c), (int, float)):
    #     raise TypeError("参数类型有误!")
    temp = b*b - 4*a*c
    print(temp)
    if temp < 0:
        print('无解')
    elif temp == 0:
        print('唯一解: ', -b/2*a)
    else:
        x1 = (-b + math.sqrt(temp))/(2 * a * c)
        x2 = (-b - math.sqrt(temp))/(2 * a * c)
        print('两个根分别为: %.2f, %.2f' %(x1, x2))

quadratic(3, 6, 9)

#   默认参数, 注意: 使用默认参数时, 必选参数在前, 摩恩参数在后, 否则报错, 多个参数时, 把变化小的参数放在后面, 变化大的放在前面
def power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
print(power(3, 3), power(3))


def enroll(name, gender, age=6, city='shenqiu'):
    print('name:', name)
    print('gender', gender)
    print('age:', age)
    print('city:', city)
    return

enroll('Sarah', 'F')

enroll('Bod', 'M', 7)

enroll('Helly', 'F', city='zhoukou')

#   默认参数必须指向不可变的对象, 否则会有大坑, 例:
def add_end(L=[]):
    L.append('END')
    return L
add_end()
add_end()
print(add_end())

print([add_end([3, 5])])

#   修改上面函数为:
def add_end(L=None):
    if L is None:
        L = []
        L.append('END')
        return L

add_end()
add_end()
print(add_end())

#   可变参数, *
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return  sum

print(calc(1, 2, 3))

#   如果已经有一个list或者tuple, 可以这样, *listName, *tupleName
nums = [2, 3, 6]
print(calc(*nums))



































































