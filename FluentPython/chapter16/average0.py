#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

#利用协程计算平均值
def coro_avg():
    total = 0
    count = 0 
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


#创建协程对象
avg = coro_avg()
#激活协程
next(avg)

for i in range(0,20,5):
    print(avg.send(i))


    

