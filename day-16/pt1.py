f = open("input","r")
lines = f.readlines()
f.close()

hex_transmission = lines[0].strip()
transmission = ""

htob = {'0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'}

btoh = {}

def bin_to_dec(b):
    b = list(map(int,list(b)))
    o = 0
    i = 0
    while len(b) > 0:
        o += (b.pop() << i)
        i += 1
    return o

for h,b in htob.items():
    btoh[b] = h

for i in hex_transmission:
    transmission += htob[i]

def parse(s):
    start = 0
    total = [0]
    recursive_parse(s,total,start)
    return total[0]

def recursive_parse(s,total,start):
    version = s[start:start+3]
    total[0] += bin_to_dec(version)
    ID = s[start+3:start+6]
    if ID == '100':
        i = start + 6
        num = ''
        while True:
            substr = s[i:i+5]
            num += substr[1:]
            i += 5
            if substr[0] == '0':
                break
        return i
    else:
        vals = []
        if s[start+6] == '0':
            i = start + 7
            length = bin_to_dec(s[i:i+15])
            i += 15
            j = i
            while j < length + i:
                j = recursive_parse(s,total,j)
            return length + i
        else:
            i = start + 7
            number = bin_to_dec(s[i:i+11])
            i += 11
            for j in range(number):
                i = recursive_parse(s,total,i)
            return i

print(parse(transmission))

