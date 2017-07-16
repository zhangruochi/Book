#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


#弱引用
import weakref
a_set = {0,1}

wref = weakref.ref(a_set)
print(wref())

a_set = {0,1,2}
#弱引用 None
print(wref())


class cheese:
    def __init__(self,kind):
        self.kind = kind

    def __repr__(self):
        return "cheese(%r)" % self.kind    


import weakref

stock = weakref.WeakValueDictionary()       
catalog = [cheese("red"),cheese("blue"),cheese("orange"),cheese("milk")]

for cheese_ in catalog:
    stock[cheese_.kind] = cheese_

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese_
print(sorted(stock.keys()))   


"""
test = [cheese("red"),cheese("blue"),cheese("orange"),cheese("milk")]
for _ in test:
    a = _

del test
del _
def a

try:
    print(a)
except:
    pass    
"""



