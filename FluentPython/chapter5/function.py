#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)

"""
print(factorial(42))
print(factorial.__doc__)
help(factorial)
"""


#--------高阶函数-------

#1，根据反向拼写排序

def reverse(word):
    return word[::-1]
fruits = ["raspberry","strawberry","banana","apple"]
fruits.sort(key = reverse)
print(fruits)


#map filter reduce
print(list(map(factorial,range(6))))
print([factorial(n) for n in range(6)])

print(list(map(factorial,filter(lambda n:n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2 ])

from functools import reduce
from operator import add
print(reduce(add,range(6)))
print(sum(range(6)))

#all any
print(all(range(6)))
print(any(range(6)))


#lambda
fn = lambda word: word[::-1]
print(fn("word"))

fruits = ["raspberry","strawberry","banana","apple"]
print(sorted(fruits,key = lambda word : word[::-1]))



#判断可调用对象
print([callable(fn) for fn in (abs , str, 13)])

#自定义可调用对象
import random
class BingoCage:
    def __init__(self,items):
        self.__items = list(items)
        random.shuffle(self.__items)

    def pick(self):
        try:
            return self.__items.pop()    
        except IndexError:
            raise LookupError("empty!")

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))                    
print(bingo.pick())
print(bingo())




# 函数参数问题   添加注解(最常用的注解是 类 和 字符串)
def func(name:str,*content,cls: "int > 0" = 0, **attr) -> str:
    print("name: " + str(name))
    print("*content: " + str(content))
    print("cls: " + str(cls))
    print("**attr: " + str(attr))

print("")
func(1,2,3,4,cls = 5, a = 6, b = 7)
#print(dir(func))

from inspect import signature
sig = signature(func)
print(sig)
print(func.__annotations__)


"""
name: 1
*content: (2, 3, 4)
cls: 5
**attr: {'a': 6, 'b': 7}
(name:str, *content, cls:'int > 0'=0, **attr) -> str
{'name': <class 'str'>, 'cls': 'int > 0', 'return': <class 'str'>}

"""



#函数式编程  主要用 operator 和 functools 
from operator import attrgetter
from collections import namedtuple

School = namedtuple("School","name loc")
jilin = School("jilin","changchun")
changan = School("changan","xian")

Person = namedtuple("Person","name age school")
zhangruochi = Person("zhangruochi",23,jilin)
lixoayue = Person("lixiaoyue",22,changan)


name_list = [zhangruochi,lixoayue]
print(sorted(name_list,key = attrgetter("age")))

print(sorted(name_list,key = attrgetter("school.loc"), reverse = True))



#functools partial  冻结参数
from functools import partial
from operator import mul
triple = partial(mul,3)
print(triple(7))










