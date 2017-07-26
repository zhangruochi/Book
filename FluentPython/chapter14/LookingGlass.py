#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "ZHANGRUOCHI"

    def reverse_write(self,text):
        self.original_write(text[::-1])

    
    def __exit__(self,exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("please do not divide by zero")
            return True


with LookingGlass() as what:
    print("fuck")
    text = what
    print(what)

print(what)    
print(text)      
print("-"*40)


#把迭代器对象转化为管理器对象
import contextlib

@contextlib.contextmanager
def lookingglass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write 
    msg = ''

    try:
        yield "ZHANGRUOCHI" 
    except ZeroDivisionError:
        msg = "please do not divide by zero"
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


with lookingglass() as what:
    print("fuck")
    text = what
    print(what)

print(what)    
print(text)      
print("-"*40)



#基于类的上下文管理器
from contextlib import ContextDecorator
class mycontext(ContextDecorator):
    def __enter__(self):
        print("Starting")
        return "enter"

    def __exit__(self,*exec):
        print("Finishing")
        return False

@mycontext() 
def function():
    print("fuck you!")       
function()
print("-"*40)
with mycontext() as string:
    print(string)
    


