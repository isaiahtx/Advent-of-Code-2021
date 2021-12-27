f = open("input","r")
lines = f.readlines()
f.close()

scores = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

opening = ['(','[','{','<']
closing = [')',']','}','>']

open_to_close = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

output = 0

for line in lines:
    q = []
    for i in range(len(line)):
        if line[i] in opening:
            q.append(line[i])
        elif line[i] in closing:
            removed = q.pop()
            if (open_to_close[removed] != line[i]):
                print("Expected",open_to_close[removed],end=", ")
                print("but found",line[i],"instead")
                output += scores[line[i]]
                break
        else:
            break
            
print()
print(output)