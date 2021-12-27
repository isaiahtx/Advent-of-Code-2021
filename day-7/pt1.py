import re
import math
import copy
import time
import timeit

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
        curr_cost += abs(p-q)
    if curr_cost < cost:
        cost = curr_cost
        best = p

print(p)
print(cost)



