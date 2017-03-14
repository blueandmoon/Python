
#   参数检查, 不符合格式的报错
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


#   如果想定义一个什么事都不做的空函数, 可以使用pass语句, pass可以用来作为占位符, 让代码正常运行, 等想好怎么写了再写函数
def nop():
    pass