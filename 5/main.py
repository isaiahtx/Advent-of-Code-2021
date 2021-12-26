import re
import math

f = open("input","r")
unformatted_lines = f.readlines()
f.close()

max_x = 0
max_y = 0

lines = []

for q in unformatted_lines:
    print(q)

    l = list(map(int,re.split(',| -> |\n',q)[:4]))
    lines.append(l)

    print(l)

    if l[0] > max_x:
        max_x = l[0]
    if l[2] > max_x:
        max_x = l[2]
    if l[1] > max_y:
        max_y = l[1]
    if l[3] > max_y:
        max_y = l[3]

max_x += 1
max_y += 1

table = []

for i in range(max_y):
    table.append([0] * max_x)

for l in lines:
    if (l[0] == l[2]):
        if (l[1] <= l[3]):
            for j in range(l[3] - l[1] + 1):
                y = l[0]
                x = l[1] + j
                table[x][y] += 1
        else:
            for j in range(l[1] - l[3] + 1):
                y=l[0]
                x=l[3]+j
                table[x][y] += 1
    elif (l[1] == l[3]):
        if (l[0] <= l[2]):
            for j in range(l[2] - l[0] + 1):
                y=l[0]+j
                x=l[1]
                table[x][y] += 1
        else:
            for j in range(l[0] - l[2] + 1):
                y=l[2]+j
                x=l[1]
                table[x][y] += 1
    else:
        y1 = l[0]
        x1 = l[1]
        y2 = l[2]
        x2 = l[3]

        if x2 >= x1:
            xi = 1
        else:
            xi = -1

        if y2 >= y1:
            yi = 1
        else:
            yi = -1
        
        while True:
            table[x1][y1] += 1
            if x1 == x2:
                break
            x1 += xi
            y1 += yi


num = 0

for t in table:
    print(t)

for t in table:
    for e in t:
        if e > 1:
            num += 1

print(num)

