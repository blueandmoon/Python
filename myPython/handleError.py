import logging
logging.basicConfig(level=logging.INFO)
print('-----------------------------------分割线---------------------------错误处理与bug调试-------------------------------')

#   高级语言内部都内置了一套try...except...finally的错误处理机制
try:
    print('trying...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('end')

#   当我们认为某些代码可能会错时, 就可以用try来运行这段代码, 如果执行出错, 则后续代码不会继续执行, 而是直接跳转至错误处理代码, 即except
#   语句块, 执行完except后, 如果有finally语句块, 则执行finally语句块, 至此, 执行完毕

#   错误有很多种, 可以用不同的except语句块来处理
try:
    print('trying...')
    r = 10 / int('a')
    print('result: ', r)
except ValueError as e:
    print('ValueError: ', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError: ', e)
finally:
    print('finally...')
print('END')

#   Python的错误也是class, 所有的错误类型都继承自BaseException, 所以在使用except时需要注意的是, 它不但捕获该类型的错误, 还把其子类也'一网打尽'
def foo():
    pass

try:
    foo()
    print('___')
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
#   第二个except永远也捕获不到UnicodeError, 因为UnicodeError是ValueError的子类, 如果有, 也被第一个except给捕获了

#   使用try...except捕获错误还有一个好处, 就是可以跨越多层调用, 比如函数main()调用foo(), foo()调用bar, 结果bar()出错了, 这时, 只要
#   main()捕获到了, 就可以处理:
def foo1(s):
    print(s)
    return 10 / int(s)

def bar(s):
    return foo1(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error: ', e)
    finally:
        print('finally...')

main()

#   只需要在合适的层次捕获错误就可以了

#   调用堆栈
#   如果错误没有被捕获, 它会一直往上抛, 最后被Python解释器捕获, 打印一个错误信息, 然后程序退出, eg:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

# main()

#   Python内置的logging模块可以记录错误信息: import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

# main()
print('End')
#   这样, 程序打印完错误信息后会继续执行, 并正常退出
#   通过配置, logging还可以把错误记录到日志文件里, 方便排查


#   抛出错误, 错误是class, 捕获错误就是捕获到该class的一个实例, 我们自己编写的函数也可以抛出错误
#   如果要抛出错误, 首先根据需要, 可以定义一个错误的class, 选择好继承关系, 然后, 用raise语句抛出一个错误的实例:
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise  FooError('invalid valuue: %s' % s)
    return 10 / n

# foo('0')  //  会抛出错误

#   来看另一种错误处理方式:
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

# bar()


print('----------------------------------------分割线-----------------------------调试-----------------------------------')

#   1. 是直接print()
#   2. 断言, 凡是print都可以用断言assert来代替
def foo(s):
    n = int(s)
    assert  n != 0, 'n is zero!'
    return 10 / n
def main():
    foo('0')
# main()

#   assert的意思是, 表达式 n != 0 应该是true, 否则, 根据程序运行的逻辑, 后面的代码肯定会出错
#   如果断言失败, assert语句本身就会抛出AssertionError
#   程序中如果到处都是assert也不太好, 不过, 启动Python解释器的-o参数来关闭assert
#   $ python3 -O err.py 然而, 并没有什么卵用, why

#   3. logging: 和assert相比, logging不会抛出错误, 而且可以输出到文件 import logging
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#   在import logging下边再加上logging.basicConfig(level=logging.INFO), 就可以看到输出日志了
#   logging允许记录信息的级别, 有debug, info, warning, error等几个级别, 当我们指定level=INFO时, logging.debug就不起作用了, 其它类似
#   这样我们就可以放心地输出不同级别的信息, 也不用删除, 最后统一控制输出哪个级别的信息
#   logging的另一个好处是通过简单的配置, 一条语句可以同时输出到不同的地方, 比如console和文件

#   4. pdb, Python的调试器pdb, 让程序以单步方式运行, 可随时查看运行状态








































































































































































































































































