#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x,self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({},{})".format(class_name,*self)

    def __str__(self):
        return str(tuple(self))    

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode,self)))

    def __eq__(self,other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmathod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast[typecode])
        return cls(*memv)    





point = Vector2d(3,4)   
print(point)    
print(tuple(point))   
print(bytes(point))      


