#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

#生成器表达式
symbols = "zhangruochi"
symbols_ascii = tuple(ord(s) for s in symbols if ord(s) > 70)
print(symbols_ascii)


import array
symbols_ascii = array.array("I",(ord(s) for s in symbols))
print(symbols_ascii)



