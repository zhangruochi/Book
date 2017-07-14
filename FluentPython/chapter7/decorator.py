#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print("running func1()")

@register
def f2():
    print("running func2()")        

@register
def f3():
    print("runing func3()")



def main():
    print("runing main()")    
    print("registry ->",registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()        
