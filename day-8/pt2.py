f = open("input","r")
unformatted_lines = f.readlines()
f.close()

lines = []

for line in unformatted_lines:
    lines.append([line.split(" | ")[0].strip().split(),line.split(" | ")[1].strip().split()])

output = 0

for line in lines:    
    numcodes = [''] * 10

    val = 0

    for i in range(len(line[0])):
        line[0][i] = ''.join(sorted(line[0][i]))

    for i in range(len(line[1])):
        line[1][i] = ''.join(sorted(line[1][i]))

    for i in range(len(line[0])):
        if len(line[0][i]) == 2:
            numcodes[1] = line[0][i] # 1
        elif len(line[0][i]) == 7:
            numcodes[8] = line[0][i] # 8
        elif len(line[0][i]) == 4:
            numcodes[4] = line[0][i] # 4
        elif len(line[0][i]) == 3:
            numcodes[7] = line[0][i] # 7
    
    for i in range(len(line[0])):
        if len(line[0][i]) == 6: # could be 6, 9, or 0.
            if ((numcodes[4][0] in line[0][i]) and 
               (numcodes[4][1] in line[0][i]) and 
               (numcodes[4][2] in line[0][i]) and 
               (numcodes[4][3] in line[0][i])):
                numcodes[9] = line[0][i] # 9
            elif (numcodes[1][0] in line[0][i]) and (numcodes[1][1] in line[0][i]):
                numcodes[0] = line[0][i] # 0
            else:
                numcodes[6] = line[0][i] # 6

    for i in range(len(line[0])): # we want to do length 5 characters last        
        if len(line[0][i]) == 5: # could be 2, 3, or 5.
            if (numcodes[1][0] in line[0][i]) and (numcodes[1][1] in line[0][i]):
                numcodes[3] = line[0][i]
            elif ((line[0][i][0] in numcodes[6]) and 
                 (line[0][i][1] in numcodes[6]) and 
                 (line[0][i][2] in numcodes[6]) and 
                 (line[0][i][3] in numcodes[6]) and 
                 (line[0][i][4] in numcodes[6])):
                numcodes[5] = line[0][i]
            else:
                numcodes[2] = line[0][i]
    
    for i in range(len(line[1])):
        for j in range(10):
            if line[1][i] == numcodes[j]:
                break
        
        val *= 10
        val += j

    output += val

    print(line[0])
    print(numcodes)
    print(val)
    print()

print()
print(output)


