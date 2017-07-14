#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

class Averager:
    def __init__(self):
        self.series = []

    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)



def make_averager():
    series = []
    def averager(new_value):
        #包含自由变量的绑定
        series.append(new_value)
        return sum(series)/ len(series)

    return averager    



def make_averager_2():
    count = 0
    total = 0
    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager    


if __name__ == '__main__':
    avg = Averager()
    print(avg(10))    
    print(avg(11))   

    print("......")

    avg_2 = make_averager()
    print(avg_2(10))
    print(avg_2(11))

    print("")
    #局部变量
    print(avg_2.__code__.co_varnames)
    #自有变量
    print(avg_2.__code__.co_freevars)

