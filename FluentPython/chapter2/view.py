#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


import array

#signed short
numbers = array.array("h",[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

print(memv.tolist())

#字节表示
memv_oct = memv.cast('B')
print(memv_oct.tolist())

#把占有两个字节的整数高字节改成了4
memv_oct[5] = 4
print(numbers)