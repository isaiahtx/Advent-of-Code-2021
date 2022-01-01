# strategy taken from reddit to count pairs

f = open("input","r")
lines = f.readlines()
f.close()

pairs = {}
rules = {}
letters = {}

def add(key,value,dictionary):
    if key in dictionary.keys():
        dictionary[key] += value
    else:
        dictionary[key] = value

template = lines[0].strip()

final_char = template[-1]

for i in range(2,len(lines)):
    line = lines[i].strip().split(' -> ')
    rules[line[0]] = line[1]

for i in range(len(template) - 1):
    add(template[i:i+2],1,pairs)

for i in range(40):
    temp_pairs = {}
    
    for pair in pairs.keys():
        if pair in rules.keys():
            if pairs[pair] == 0:
                continue
            num = pairs[pair]
            pairs[pair] = 0
            add(pair[0] + rules[pair],num,temp_pairs)
            add(rules[pair] + pair[1],num,temp_pairs)
    
    for pair in temp_pairs.keys():
        add(pair,temp_pairs[pair],pairs)

for pair in pairs.keys():
    add(pair[0],pairs[pair],letters)

add(final_char,1,letters)

print(max(letters.values()) - min(letters.values()))
        

