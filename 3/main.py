gl = []
el = []

f = open("input","r")
lines = f.readlines()
f.close()

length = len(lines)


for i in range(len(lines[0])):
    if lines[0][i] != '\n':
        gl.append(0)

for l in lines:
    i = -1
    for c in l:
        i += 1
        if c == '\n':
            break
        elif c == '1':
            gl[i] = gl[i] + 1

for i in range(len(gl)):
    if 2*gl[i] >= length:
        gl[i] = 1
    else:
        gl[i] = 0

x = []
y = []

fin_x = ""
fin_y = ""

for i in range(len(gl)):
    x.append([])
    y.append([])
    if i == 0:
        for j in range(len(lines)):
            if lines[j] == "\n":
                break

            if int(lines[j][i]) == int(gl[i]):
                x[i].append(lines[j])
            else:
                y[i].append(lines[j])
    else:
        g = 0
        h = 0
        for j in x[i-1]:
            if j[i] == "1":
                g += 1
        
        for j in y[i-1]:
            if j[i] == "1":
                h += 1
        
        if 2*g >= len(x[i-1]):
            g = 1
        else:
            g = 0

        if 2*g >= len(y[i-1]):
            h = 1
        else:
            h = 0

        for j in x[i-1]:
            if int(j[i]) == g:
                x[i].append(j)

        for j in y[i-1]:
            if int(j[i]) != h:
                y[i].append(j)

        if len(x[i]) == 1:
            fin_x = x[i][0]
        if len(y[i]) == 1:
            fin_y = y[i][0]


print(fin_x)
print(fin_y)

os = 0
ls = 0 

def conb(x):
    o = 0
    for i in x:
        try:
            i = int(i)
            assert (i == 0) or (i == 1)
        except:
            break

        if i == 0:
            o *= 2
        else:
            o *= 2
            o += 1
    return o

print(conb(fin_x)*conb(fin_y))

















