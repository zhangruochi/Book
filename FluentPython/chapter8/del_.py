#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

#注册一个回调函数 在销毁时调用

import weakref

s1 = {1,2,3}
s2 = s1

def bye():
    print("Gone with wind... ")

ender = weakref.finalize(s1,bye)
print(ender.alive)

del s1
print(ender.alive)

s2 = "spam"
print(ender.alive)





