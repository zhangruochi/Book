#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


from array import array
import math

class Vector2d:
    #不仅减少内存 还可以用__slots__限制使用的属性
    __slots__ = ("__x","__y")
    typecode = 'd'

    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
         
    @property
    def y(self):
        return self.__y
    
    #hash 函数最好采用位运算符混合所有属性的 hash 值    
    def __hash__(self):
        return hash(self.__x) ^ hash(self.__y)    
        

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

    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast[typecode])
        return cls(*memv)    

    def angle(self):
        return math.atan2(self.y,self.x)

    #如果以'p'结尾，使用极坐标    
    def __format__(self,fmt_spec=''):

        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self),self.angle())
            outer_fmt = '<{},{}>'
        else:
            coords = self
            outer_fmt = '({},{})'

        components = (format(c,fmt_spec) for c in coords)

        return outer_fmt.format(*components)








point = Vector2d(3,4)   
print(point)
#print(point.__dict__)
print(point)    
print(tuple(point))   
print(bytes(point))    

print(format(Vector2d(1,1),'.3f'))
print(format(Vector2d(1,1),'.3ep'))








