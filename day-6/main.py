import re
import math
import copy
import time
import timeit

f = open("input","r")
lines = f.readlines()
f.close()

def sim_old(l,n):
    for i in range(n):
        for j in range(len(l)):
            if l[j] == 0:
                l[j] = 6
                l.append(8)
            else:
                l[j] -= 1
    return(len(l))

def sim(l, n):  # l is list of fish, n is number of days. Returns new list.
    total = len(l)
    weekday = [0,0,0,0,0,0,0]
    buff = [0,0,0,0,0,0,0]

    for i in range(len(l)):
        weekday[(l[i] + 1) % 7] += 1

    for i in range(n+1):
        total += weekday[i%7]
        buff[(i+2)%7] += weekday[i%7]
        weekday[i%7] += buff[i%7]
        buff[i%7] = 0

    return(total)

l = list(map(int,lines[0].strip().split(',')))

print(sim(l,256))

