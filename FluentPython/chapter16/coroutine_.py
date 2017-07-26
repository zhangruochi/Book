#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


def simple_coroutine():
    print("-> coroutine started")
    x = yield "fuck"
    print("-> coroutine received: ", x)



#生成器产出 None
for x in simple_coroutine():
    print(x)    
"""
-> coroutine started
None
-> coroutine received:  None
"""


#先产出，再暂停，然后再接受值，最后赋值
print("-"*40)
test = simple_coroutine()
#激活协程
text = next(test) 
print(text)
test.send(42)

