import math

f = open("input","r")
lines = f.readlines()
f.close()

template = lines[0].strip()

pairs = {}

letters = {}

for i in template:
    if i not in letters.keys():
        letters[i] = 1
    else:
        letters[i] += 1

for i in range(2,len(lines)):
    line = lines[i].strip().split(' -> ')
    pairs[line[0]] = line[1]
    if line[1] not in letters.keys():
        letters[line[1]] = 0

num = int(input("how many times: "))

to_add = []

for i in range(num):
    for j in range(len(template) - 1):
        substr = template[j:j+2]
        if substr in pairs.keys():
            to_add.append([j+1,pairs[substr]])
    
    while len(to_add) > 0:
        add = to_add.pop()
        template = template[:add[0]] + add[1] + template[add[0]:]
        letters[add[1]] += 1

values = list(letters.values())

values.sort()

print(values[len(values) - 1] - values[0])

