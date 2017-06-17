#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

import collections

class MyDict(collections.UserDict):
    #被__getitem__调用
    def __missing__(self,key):
        if not isinstance(key,str):
            raise TypeError("key should be string")
        else:
            return list()

    def get(self,key, default):
        try:
            return self[key]
        except:
            return default

    def __contains__(self,key):
        return str(key) in self.data

    
    def __setitem__(self,key,item):
        self.data[str(key)] =  item


test = MyDict()
print( test["a"] )   
print( 1 in test )   


from types import MappingProxyType
d = {1 : "A"}
d_proxy = MappingProxyType(d)                          
print(d_proxy)
d.update({2: "B"})
print(d_proxy)
try:
    d_proxy[3] = "C"
except:
    print("error")    


