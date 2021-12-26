import re
import math
import copy

f = open("input","r")
lines = f.readlines()
f.close()

def sim(l, n):  # l is list of fish, n is number of days. Returns new list.
    r = copy.deepcopy(l)
    
    for i in range(n):
        length = len(r)
        for j in range(length):
            if r[j] == 0:
                r[j] = 6
                r.append(8)
            else:
                r[j] -= 1
    return r

l = list(map(int,lines[0].strip().split(',')))
print(l)
print(len(sim(l,80)))

