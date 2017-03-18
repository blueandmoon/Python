from types import MethodType

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
























































































































































































