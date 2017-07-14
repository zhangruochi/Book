#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' %(elapsed,name,arg_str,result))
        return result
    return clocked

"""
#注意下面的写法为什么不行
def clock_2(func):
    t0 = time.perf_counter()
    result = func(*args)
    elapsed = time.perf_counter() - t0
    print("using time {}".format(elapsed))
    return func
"""    


@clock
def snooze(seconds):
    time.sleep(seconds)
    return "finished"

@clock
def factorial(n):
    return 1 if n < 2 else  n * factorial(n-1)


#引入缓存技术，会保存最耗时的函数的结果以避免重复计算
from functools import lru_cache

@lru_cache()
@clock
def fabonacci(n):
    return n if n < 2 else fabonacci(n-1) + fabonacci(n - 2)        


def best_fabonacci(n):
    cache = {}
    def fabonacci(n):
        if n in cache:
            return cache[n]
        else:    
            if n < 2:
                cache[n] = n
                return n
            cache[n] = fabonacci(n-1) + fabonacci(n-2)
            return fabonacci(n - 1) + fabonacci(n - 2)   
    result = fabonacci(n)
    print(cache)
    return result


#单分派泛函数
import html
from functools import singledispatch
import numbers
from collections import abc


@singledispatch
def htmlize(obj):
    #escape Convert the characters &, < and > in string s to HTML-safe sequences
    content = html.escape(repr(obj))
    return "<pre>{} </pre>".format(content)



@htmlize.register(str)
def _(text):
    content = html.elapse(text).replace("\n","<br>\n")
    return "<p>{0}</p>".format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return "<pre>{0} (0x{0:x}) </pre>".format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return "<ul>\n<li>" + inner + "</li>\n</ul>"



#为了方便给装饰器传递额外的参数 需要创建装饰器工厂函数
registry = set()
def register(active = True):
    def decorator(func):
        if active:
            #print("register actived....")
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorator

@register(active = True) 
def f1():
    pass

@register(active = False)
def f2():
    pass

@register(active = True)
def f3():
    pass           




            
        




if __name__ == '__main__':
    #snooze(0.123)
    #print(fabonacci(100))
    #print(best_fabonacci(30))
    print(registry)
