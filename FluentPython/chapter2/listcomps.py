#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


#列表推倒
symbols = "zhangruochi"
symbols_ascii = [ord(s) for s in symbols if ord(s) > 70]
print(symbols_ascii)


#filter map
symbols_ascii = list(filter(lambda x:x>70,map(ord,symbols)))
print(symbols_ascii)

