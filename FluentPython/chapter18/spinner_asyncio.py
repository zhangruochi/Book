#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


import asyncio
import itertools
import sys

class Signal:
    go = True


@asyncio.coroutine
def spin(msg):
    write,flush = sys.stdout.write,sys.stdout.flush
    for char in itertools.cycle("|/-\\"):
        status = char + ' ' + msg
        write(status)
        flush()
        #回退符
        write("\b" * len(status))
        try:
            yield from asyncio.sleep(.1) 
        except asyncio.CancelledError:
            break                
    write(' ' * len(status) + '\b' * len(status))        

@asyncio.coroutine
def slow_function():
    #假装 IO 等待一段时间
    yield from asyncio.sleep(3)
    return 43

@asyncio.coroutine
def supervisor():
    spinner = asyncio.async(spin("thinking!"))
    print("spinner object: ",spinner)
    result = yield from slow_function()
    spinner.cancel()
    return result


def main():
    #获取事件循环引用
    loop = asyncio.get_event_loop()
    #驱动 supervisor 协程，让它运行完毕
    result  = loop.run_until_complete(supervisor())
    loop.close()
    print("Answer: ", result)


if __name__ == '__main__':
    main()       