f = open("input","r")
lines = f.readlines()
f.close()
xmin,xmax = lines[0].strip().split('=')[1].split(',')[0].split('..')
ymin, ymax = lines[0].strip().split('=')[-1].split('..')
xmin = int(xmin)
xmax = int(xmax)
ymin = int(ymin)
ymax = int(ymax)

def sign(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    if x < 0:
        return -1

def sim(vx,vy,xmin,xmax,ymin,ymax):
    x = 0
    y = 0
    while (y >= ymin or vy >= 0):
        if (xmin <= x <= xmax) and (ymin <= y <= ymax):
            return 1
        x += vx
        y += vy
        vx += (-1 * sign(vx))
        vy -= 1

    return 0

total = 0

for vx in range(xmax + 1):
    for vy in range(ymin - 1,(-1 * ymin) + 1):
        total += sim(vx,vy,xmin,xmax,ymin,ymax)

print(total)
