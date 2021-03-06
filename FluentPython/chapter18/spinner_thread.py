#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

import threading
import itertools
import time
import sys

"""
for i in range(5):
    sys.stdout.write(str(i))
    #sys.stdout.flush()
    time.sleep(1)
"""

class Signal:
    go = True


def spin(msg,signal):
    write,flush = sys.stdout.write,sys.stdout.flush
    for char in itertools.cycle("|/-\\"):
        status = char + ' ' + msg
        write(status)
        flush()
        #回退符
        write("\b" * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\b' * len(status))        

def slow_function():
    time.sleep(3)
    return 43

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target = spin, args = ("thinking!", signal))
    print("spinner object: ",spinner)
    spinner.start()

    #主线程等待，此时派生线程仍然在运行
    result = slow_function()
    #给派生线程发送终止消息
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print("Answer: ", result)


if __name__ == '__main__':
    main()       



    


