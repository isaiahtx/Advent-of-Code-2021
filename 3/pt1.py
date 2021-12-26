gl = []
el = []

f = open("input","r")
lines = f.readlines()
f.close()

length = len(lines)

count = 0

for i in range(len(lines[0])):
    print(lines[0][i])
    if lines[0][i] != '\n':
        count += 1
        gl.append(0)


print('---')
print(count)
print('---')

for l in lines:
    i = -1
    for c in l:
        i += 1
        if c == '\n':
            break
        elif c == '1':
            gl[i] = gl[i] + 1

g = 0
e = 0

for i in gl:
    if 2*i >= length:
        print(1,end="")
        g *= 2
        g += 1
        e *= 2
    else:
        print(0,end="")
        g *= 2
        e *= 2
        e += 1

print()

print(g)
print(e)
print(g*e)

