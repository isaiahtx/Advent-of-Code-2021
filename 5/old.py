import re

f = open("input","r")
unfiltered_lines = f.readlines()
f.close()

lines = []

max_x = 0
max_y = 0

for l in unfiltered_lines:
    l = list(map(int,re.split(',| -> |\n', l)[:4]))
    if (l[0] == l[2]) or (l[1] == l[3]):
        lines.append(l)
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
    else:
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

num = 0

for t in table:
    for e in t:
        if e > 1:
            num += 1

print(num)

