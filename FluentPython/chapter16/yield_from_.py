#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

def gen():
    yield from "AB"
    yield from range(1,3)

print(list(gen()))  

def chain(*iterables):
    for it in iterables:
        yield from it


s = "ABC"          
t = tuple(range(3))
print(list(chain(s,t)))
print("-"*40)


from collections import namedtuple

Result = namedtuple("Result","count averge")

#子生成器
def averager():
    total = 0
    count = 0
    averge = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        averge = total / count
    return Result(count,averge)

#委派生成器
def grouper(results, key):
    while True:
        results[key] = yield from averager()


#客户端代码
def main(data):
    results = {}
    for key, values in data.items():
        #生成委派生成器对象
        group = grouper(results,key)
        #激活委派生成器
        next(group)
        for value in values:
            #委派生成器在yield from 出暂停，调用方可以直接把数据发送给子生成器，
            #子生成器再把产出的值发送给调用方
            group.send(value)
        group.send(None)
    report(results)                            
        
def report(results):
    for key,result in sorted(results.items()):
        group,unit = key.split(";")  
        print("{} {} averging {}".format(result.count,group,result.averge,unit))


data = {
    "girls;kg": list(range(0,20)),
    "girls;m": list(range(0,10)),
    "boys;kg": list(range(5,25)),
    "boys;m": list(range(5,15)),
}   


main(data)           
