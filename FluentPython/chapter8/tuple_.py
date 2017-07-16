#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


a = (1,2,3,[4,5])
b = (1,2,3,[4,5])

print(a==b)
print(a is b)

print(id(a[3]),a[3])
a[3].extend([99])
print(id(a[3]),a[3])

print(a == b)
print(a is b)