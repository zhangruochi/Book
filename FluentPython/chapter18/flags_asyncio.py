#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com



import os
import time
import sys
import asyncio
import aiohttp

import requests  # <1>

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'http://flupy.org/data/flags'  # <3>

DEST_DIR = 'downloads/'  # <4>


def save_flag(img, filename):  # <5>
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def show(text):  # <7>
    print(text, end=' ')
    sys.stdout.flush()        

@asyncio.coroutine
def get_flag(cc):  # <6>
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    #客户代码通过 yield from 把职责委托给协程，以便异步执行
    resp = yield from aiohttp.request("GET",url)
    #读取相应内容也是单独的异步操作
    image = yield from resp.read()
    return image

@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flag(image,cc.lower() + ".gif")
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    #有期物或者协程构成的可迭代对象
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    #wait 不是阻塞型函数，而是一个协程，等待传给它的协程运行完毕
    wait_coro = asyncio.wait(to_do)
    #执行时间循环，直到 wait_coro运行结束
    res,_ = loop.run_until_complete(wait_coro)
    return len(res)    

def main(download_many):  # <10>
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))

if __name__ == '__main__':
    main(download_many)    



