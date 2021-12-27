import math

f = open("input","r")
lines = f.readlines()
f.close()

def print_page(page):
    for row in page:
        for en in row:
            if (en==1):
                print('█',end='')
            else:
                print(' ',end='')
        print()

cols = 0
rows = 0

start_fold_instructions = 0

for line in lines:
    start_fold_instructions += 1
    if line == '\n':
        break
    l = list(map(int,line.strip().split(',')))
    if l[1] > rows:
        rows = l[1]
    if l[0] > cols:
        cols = l[0]

rows += 1
cols += 1

page = []

for i in range(rows):
    page.append([0] * cols)

for line in lines:
    if line == '\n':
        break
    l = list(map(int,line.strip().split(',')))
    page[l[1]][l[0]] = 1

def fold(page,line):
    rows = len(page)
    cols = len(page[0])
    if line[11] == 'x':
        new_length = 0
        crease = int(line.strip()[13:])
        for i in range(1,cols-crease):
            new_length += 1
            if crease-i >= 0:
                for j in range(rows):
                    page[j][crease-i] = page[j][crease-i] | page[j][crease+i]
            else:
                print("this shouldn't be here")
        for i in range(len(page)):
            page[i] = page[i][:new_length]
        return page

    else:
        new_length = 0
        crease = int(line.strip()[13:])
        for i in range(1,rows-crease):
            new_length += 1
            if crease-i >= 0:
                for j in range(cols):
                    page[crease-i][j] = page[crease-i][j] | page[crease+i][j]
            else:
                page.insert(0,page[crease+i])
        page = page[:new_length]
        return page

count = 0

for i in range(start_fold_instructions,len(lines)):
    page = fold(page,lines[i])

print()
print_page(page)

for row in page:
    for en in row:
        count += en

print(count)
