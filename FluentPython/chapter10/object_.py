#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


from array import array
import math
import reprlib
import numbers
from functools import reduce
from operator import xor

class Vector:
    typecode = 'd'
    shortcut_name = "xyzt"

    def __init__(self,components):
        self._components = components
    
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("[") + 1:-1]
        return "Vector({})".format(components)

    def __str__(self):
        return self.__repr__()

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self,other):
        if len(self) != len(other):
            return False
        for a,b in zip(self,other):
            if a != b:
                return False
        return True            

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    #---- 支持序列协议------
    def __len__(self):
        return len(self._components)  

    
    def __getitem__(self,index):

        if isinstance(index,slice):
            return Vector(self._components[index])
        elif isinstance(index,numbers.Integral):
            return self._components[index]
        else:
            msg = "{cls} indices must be Integrals"
            raise TypeError(msg.format(cls = index.__class__))    

    
    def __getattr__(self,name):
        cls = self.__class__

        if len(name) == 1:
            pos =  self.__class__.shortcut_name.find(name)     
            if 0 <= pos < len(self._components):
                return self._components[pos]

            msg = "{.__name__} obejct has no attribute {}"
            raise AttributeError(msg.format(cls,name))

    def __setattr__(self,name,value):
        cls = type(self)

        if len(name) == 1:
            if name in cls.shortcut_name:
                error = "readonly attribute {attr_name!r}"
            elif name.islower():
                error = "can not set attribute a to z"
            else:
                error = ""
            
            if error:
                raise ArithmeticError
        super().__setattr__(name,value)
                
                                    
    def __hash__(self):
        hashes = map(hash,self._components)
        return reduce(xor,hashes)



                   


    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast[typecode])
        return cls(*memv)    

    



vector = Vector([1,2,3,4,5,6,7,8,9,10])
print(vector)
print(len(vector))
print(vector[1:5])
#print(vector[2.0])
print(vector.x)

vector.X = 1

print(vector.__dict__) 
print(hash(vector))








