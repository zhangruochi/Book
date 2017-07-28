#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

import os
import time
import sys

import requests  # <1>

from concurrent import futures

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'http://flupy.org/data/flags'  # <3>

DEST_DIR = 'downloads/'  # <4>

MAX_WORKERS = 20


def save_flag(img, filename):  # <5>
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):  # <6>
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):  # <7>
    print(text, end=' ')
    sys.stdout.flush()


def download_one(cc):
    img = get_flag(cc)
    show(cc)
    save_flag(img,cc.lower()+".gif")
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS,len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one,sorted(cc_list))
    return len(list(res))

#as_completed 这个函数的参数是一个期物列表，返回值是一个迭代器， 在期物运行结束后产出期物。
def download_many_two(cc_list):
    with futures.ThreadPoolExecutor(max_workers = 3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one,cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {} '
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            print("{} result: {}".format(future,res))
            results.append(res)

if __name__ == '__main__':
    download_many_two(POP20_CC)        
