#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

"""
import numbers

if isinstance(1.34,numbers.Real):
    print("true!")
print(repr(1.34))
"""

import abc

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回"""

    def loaded(self):
        """至少有一个元素，则返回True"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序数组，由当前元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        self.load(items)
        return tuple(sorted(items))

import random

class BingoCage(Tombola):
    
    def __init__(self,items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self,items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items) 

    def pick(self):
        try:
            return self._items.pop()       
        except IndexError:
            raise LookupError("pick error")

    def __call__(self):
        return self.pick()


#虚拟子类
from random import randrange
@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("POP ERROR")    

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))




if __name__ == '__main__':
    binggo = BingoCage([1,2,3,4,5])
    print(binggo())

    tombo = TomboList([1,2,3,4])
    tombo.load([5,6])
    print(tombo.pick())


    print(issubclass(TomboList,Tombola))




    









                