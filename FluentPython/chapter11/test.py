#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

class Test:
    @classmethod
    def fuck(cls,a):
        print("in class")
        print(a)
    """
    def fuck(self,a):
        print("in object")
        print(a)
    """


tester = Test()
tester.fuck("fuck you")        

