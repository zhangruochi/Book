#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

def gen():
    yield from "AB"
    yield from range(1,3)

print(list(gen()))  

def chain(*iterables):
    for it in iterables:
        yield from it


s = "ABC"          
t = tuple(range(3))
print(list(chain(s,t)))
