#!/usr/bin/env python3

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


#使用协程在单个线程中管理并发活动

from collections import namedtuple
import queue
import random

Event = namedtuple("Event","time proc action")

def compute_duration():
    return random.randint(10,30)



def taxi_process(ident, trips, start_time = 0):
    time = yield Event(start_time, ident, "leave garge")
    for i in range(trips):
        time = yield Event(time,ident,"pick up passenger")
        time = yield Event(time,ident,"drop off passenger")

    yield Event(time,ident,"going home") 



class Simulator:
    def __init__(self,procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self,end_time):
        #激活所有的出租车
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)    

        #仿真系统的主循环
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event   
            print("taxi: ", proc_id, proc_id * ' ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration()
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
                
        #只有当 while 语句因条件假设不成立时才调用此语句
        else:
            msg = '*** end of simulation time: {} events pending'
            print(msg.format(self.events.qsize()))            






def main():
    num_taxis = 3
    interval = 5

    taxis = {i:taxi_process(i,(i+1)*2,i * interval) for i in range(num_taxis)} 
    sim = Simulator(taxis)
    sim.run(500)


"""
time = 0
taxi = taxi_process(ident = 13, trips = 2,start_time = time)  
print(next(taxi))
time = time + 7  
print(taxi.send(time))
time = time + 23
print(taxi.send(time))
time = time + 20
print(taxi.send(time))
time = time + 25
print(taxi.send(time))
time = time + 27
print(taxi.send(time))
print("-"*40 + "\n")
"""

if __name__ == '__main__':
    main()