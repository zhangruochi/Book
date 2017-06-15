#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

from collections import namedtuple

City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo','JP','36.933',(35.6,139.7))
print(tokyo)

print(tokyo._fields)
print(tokyo._asdict())