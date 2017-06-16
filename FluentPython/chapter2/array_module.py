#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


from array import array
from random import random

floats = array('d',(random() for i in range(10**7)))
print(floats[-1])
fp = open("floats.bin","wb")
floats.tofile(fp)
fp.close()


with open("floats.bin","rb") as f:
    floats.fromfile(f,10**7)
print(floats[-1])    
