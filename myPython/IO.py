from io import StringIO
from io import BytesIO
import pickle
import json

print('-----------------------------------------分割线----------------------------文件读写--------------------------------')

#   读文件, 使用open()函数, 传入文件名和标识符
f = open('/Users/apple/Desktop/test1.txt', 'r')   #   r表示读
#   好奇怪, 从pages转为纯文本读取无碍, 但是从word转为txt就无法读取, 同是utf-8, why
print(f)

#   如果文件读取失败, 会报错, 读取成功则可调用read()方法一次读取文件的全部内容, Python把内容读到内存, 用一个str对象表示
s = f.read()
print(s)

#   最后一步是调用close()方法关闭文件. 文件使用完毕后必须关闭, 因为文件对象会占用操作系统的资源, 并且操作系统同一时间能打开的文件数量也是有限的:
f.close()

#   由于文件读写随时都有可能产生IOError, 一旦出错, 后面的f.close()就不会调用, 所以, 为了保证无论是否出错都能正确地关闭文件, 我们可以使用
#   try...finally来实现:
try:
    f = open('/Users/apple/Desktop/test1.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#   但是每次都这么写太繁琐, so, Python引入了with语句来自动帮我们调用close()方法:
with open('/Users/apple/Desktop/test1.txt', 'r') as f:
    print(f.read())

#   这和前面的try...finally是一样的, 但是代码更简洁, 且不必调用f.close()方法

#   调用read()会一次性读取文件的全部内容, 如果文件有10, 内存就爆了, so, 保险起见, 可以反复调用read(size)方法, 每次最多读取size个字节的内容
#   另外, 调用readline()可以每次读取一行的内容, 调用readlines()方法可以一次读取所有内容并按行返回list. 因此, 要根据需要决定怎么调用

#   如果文件很小, read()一次性读取最方便; 如果不能确定文件大小, 反复调用read(size)比较保险; 如果是配置文件, 调用readlines()最方便
print('------1----')
with open('/Users/apple/Desktop/test1.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip()) #   把末尾的'\n'删掉
    # L = f.readlines()
    # print(L[3])

print('---------')
with open('/Users/apple/Desktop/test1.txt', 'r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

print('---------')
with open('/Users/apple/Desktop/test1.txt', 'r') as f:
    print(f.read(5))

print('---__---------__---')

#   file-like Object
#   像open()函数返回的这种有个read()方法的对象, 在Python中统称为file-likeObject. 除了file外, 还可以是内存的字节流, 网络流, 自定义流等等.
#   file-like Object不要求从特定类集成, 只要写个read()方法就行
#   StringIO就是在内存中创建的file-like Object, 常用作临时缓冲

#   二进制文件
#   前面讲的默认都是读取本地文件, 并且是UTF-8编码的文本文件. 要读取二进制文件, 比如图片, 视频等, 用'rb'模式打开文件即可:
with open('/Users/apple/Desktop/111.png', 'rb') as f:
    print(f.read()) #   输出是十六进制表示的字节

#   字符编码
#   要读取非UTF-8编码的文本文件, 需要给open()函数传入encoding参数, 例如, 读取GBK编码的文件:(然而, 手边没有gbk文件)
with open('/Users/apple/Desktop/test2.txt', 'r', encoding='utf-8') as f:
    print(f.read())

#   遇到编码不规范的文件, 可能会遇到UnicodeDecodeError, 这种情况下, open()函数还接收一个errors参数, 表示如果遇到错误编码后如何处理, 最简单
#   的方式是直接忽略:
# print('-8888888_----')
# with open('/Users/apple/Desktop/test2.txt', 'r', encoding='utf-16', errors='ignore') as f:
#     print(f.read())
# print('-')

#   写文件
#   写文件和读文件是一样的, 唯一区别是调用open()函数时, 传入标识符'w'或者'wb'表示写文本文件或写二进制文件:
with open('/Users/apple/Desktop/test2.txt', 'w') as f:
    f.write('Hello world!')
    f.write('dier')

#   要写入特定编码的文件, 给open()传入encoding参数即可, 将字符串自动转换成指定编码

print('--------------------------------分割线--------------------------------StringIO和BytesIO---------------------------')

#   StringIO顾名思义就是在内存中读写str
#   要把str写入StringIO, 我们需要先创建一个StringIO, 然后, 像文件一样写入即可:
f = StringIO()
print(f.write('hello world!'))
print(f.write('Hi'))

print(f.getvalue()) #   getvalue()方法用于获得写入后的str
#   要读取StringIO, 可以用一个str初始化StringIO, 然后, 像读文件一样读取:
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#   BytesIO
#   StringIO操作的只能是str, 如果要操作二进制数据, 就需要使用BytesIO
#   BytesIO实现了再内存中读写bytes, 我们创建一个BytesIO, 然后写入一些bytes
f = BytesIO()
print(f.write('中文'.encode('utf-8')))

print(f.getvalue()) #   注意: 写入的不是str, 而是经过UTF-8编码的bytes

#   和StringIO类似, 可以用一个bytes初始化BytesIO, 然后, 像读文件一样读取:
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())


print('---------------------------------分割线-------------------------操作文件和目录--------------------------------------')

#   Python内置的os模块也可以直接调用操作系统提供的接口函数
import os
print(os.name)  #   操作系统类型. 如果是posix, 说明系统是Linux, Unix或Mac OS x, 如果是nt, 就是windows系统
#   要获取到详细的系统信息, 可以调用uname()函数
print(os.uname())

#   环境变量, 在操作系统中定义的环境变量, 全部保存在os.environ这个变量中
print(os.environ)

#   要获取某个环境变量的值, 可以调用os.environ.get('key'):
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

#   操作文件和目录
#   操作文件和目录的函数一部分放在os模块中, 一部分放在os.path模块中

#   查看当前目录的绝对路径:
print(os.path.abspath('.'))
#   在某个目录下创建一个新目录, 首先把新目录的完整路径表示出来:
print(os.path.join('/Users/apple/ligen/Python/myPython', 'testdir'))
#   然后创建一个目录:
# os.mkdir('/Users/apple/ligen/Python/myPython/testdir')
#   删掉一个目录:
# os.rmdir('/Users/apple/ligen/Python/myPython/testdir')

#   拆分路径:   拆分为两部分, 后一部分总是最后级别的目录或文件名
print(os.path.split('/Users/apple/ligen/Python/myPython/testdir'))

#   后一部分为文件扩展名, 这些函数都是对字符串进行操作的
print(os.path.splitext('/Users/apple/ligen/Python/myPython/testdir/a.txt'))

#   文件操作使用下面的函数, 嘉定当前目录下有一个test.txt文件:

#   对文件重命名
# os.rename('test.txt', 'test.py')
#   删除文件
# os.remove('test.pay')

#   列出当前目录下的所有目录:
print([x for x in os.listdir('.') if os.path.isdir(x)])

#   列出所有的.py文件:
print([x for  x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


print('----------------------------------------分割线----------------------------序列化-----------------------------------')

#   在程序运行过程中, 所有的变量都是存在内存中的, 等程序结束, 变量所占的内存就会被系统收回
#   我们吧变量从内存中变成可存储或传输的过程称之为序列化, 在Python中叫做pickling,
#   序列化之后, 就可以吧序列化后的内容写入磁盘, 或者通过网络出疏导别的机器上, 与反序列化对应
#   improt pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

#   pickle可以吧对象序列化为一个bytes, 然后就可以把这个bytes写入文件, 或者使用pickle.dump()直接把对象序列化后写入一个file-like Object:
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

#   从磁盘读取到内存时, 可以先把内容读取到bytes, 然后用pickle.loads()方法反序列化出对象, 也可以直接pickle.load()方法从一个file-like Object
#   中直接反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)


#   把对象转为json, improt json
d = dict(name='Bobb', age=29, score=88)
print(json.dumps(d))    #   json返回一个str
#   要把json反序列化, 使用loads()或者对应的load()方法, 前者吧JSON的字符串反序列化, 后者从file-like Object中读取字符串并反序列化
j = json.dumps(d)
print(json.loads(j))


#   JSON进阶







''






































































































































































































































































































































































































