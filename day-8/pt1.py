f = open("input","r")
lines = f.readlines()
f.close()

l = []

for line in lines:
    l.append(line.split(" | ")[1].strip().split())

count = 0

for p in l:
    for qe in p:
        we = len(qe)
        if (we == 2) or (we == 4) or (we == 3) or (we == 7):
            count += 1
            print(qe)

print(count)




