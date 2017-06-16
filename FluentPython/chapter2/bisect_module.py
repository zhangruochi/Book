#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

import bisect 

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]



NEEDLES.reverse()

for num in NEEDLES:
    position = bisect.bisect_right(HAYSTACK,num)
    print(position, end=",")


print("")
#找到成绩对应的 gradrs 
def grade_student(grade):
    return "ABCD"[bisect.bisect_left([60,70,80,90],grade)] 

print(grade_student(65))   


import random
my_list = []
for i in range(10):
    new_item = random.randrange(10 * 2)
    bisect.insort(my_list, new_item)
print(my_list)    



