f = open("input","r")
lines = f.readlines()
f.close()
xmin,xmax = lines[0].strip().split('=')[1].split(',')[0].split('..')
ymin, ymax = lines[0].strip().split('=')[-1].split('..')
xmin = int(xmin)
xmax = int(xmax)
ymin = int(ymin)
ymax = int(ymax)
n = -ymin - 1
print(int(n * (n+1) / 2))

