#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


#让协程返回值

from collections import namedtuple

Result = namedtuple("Result","count avg")

def average():
    total = 0
    count = 0
    avg = None
    while True:
        term = yield
        if term == None:
            break
        total += term
        count += 1
        avg = total / count

    return Result(count,avg)

avg = average()
next(avg)  
avg.send(10)
avg.send(20)
avg.send(30)
try:
    avg.send(None)
except StopIteration as exc:
    print(exc.value)    






