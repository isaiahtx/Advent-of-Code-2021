import re
import math
import copy
import time
import timeit

def fibs(n):
    return n * (n + 1) / 2

f = open("input","r")
lines = f.readlines()
f.close()

l = list(map(int,lines[0].strip().split(',')))

max = 0

for p in l:
    if p > max:
        max = p

best = 0
cost = 1000000000
for p in range(max+1):
    curr_cost = 0
    for q in l:
        mc = fibs(abs(p-q))
        curr_cost += mc
    
    if curr_cost < cost:
        cost = curr_cost
        best = p

print(p)
print(cost)



