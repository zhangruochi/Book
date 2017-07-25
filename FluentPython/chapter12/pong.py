#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


class A:
    def ping(self):
        print("A: ", self)


class B(A):
    def pong(self):
        print("B",self)

class C(A):
    def pong(self):
        print("C",self)


class D(B,C):
    def ping(self):
        super().ping()
        print("D: ",self)

    def pingpong(self):
        #self.ping()
        super().pong()
        C.pong(self)                        



if __name__ == '__main__':
    test = D()
    test.pingpong()        