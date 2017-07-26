#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com



class DemoException(Exception):
    """定义异常类型"""

def demo_exc_handling():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            print("handling DemoException")
        except ZeroDivisionError:
            print("ZeroDivisionError")    
        else:
            print("-> coroutine received: {}".format(x))

    raise RuntimeError("This line should never get")

from inspect import getgeneratorstate

exc = demo_exc_handling()
next(exc) 
exc.send(10)
exc.throw(ZeroDivisionError)
exc.send(20)
print(getgeneratorstate(exc))
exc.close()
#exc.send(30)

