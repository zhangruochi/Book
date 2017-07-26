#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

from functools import wraps
"""
Without the use of this decorator factory, 
the name of the example function would have been 'wrapper', 
and the docstring of the original example() would have 
been lost.
"""

def coroutine(func):
    """装饰器，预激活 func  """
    @wraps(func)
    def wrapper(*args,**kwargs):
        gen = func(*args,**kwargs) 
        next(gen)
        return gen

    return wrapper
  

@coroutine
def coro_avg():
    """calculate the average"""

    total = 0
    count = 0 
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


test = coro_avg()
print(test.__name__)

for i in range(0,20,5):
    print(test.send(i))


           