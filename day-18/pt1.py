import math

"""
A snail number will be represented as an array of solely numbers where:
    -1 represents open bracket
    -3 represents close bracket
    any other negative number is invalid
    anything other nonnegative number is a regular number
Note that storing commas is unnecessary
"""

def explode(s,l,p1,p2,r):
    if l > 0:
        s[l] += s[p1]
    if r > 0:
        s[r] += s[p2]
    s = s[:p1-1] + [0] + s[p2+2:]
    return s

def split(s,i):
    s = s[:i] + [-1,math.floor(s[i]/2),math.ceil(s[i]/2),-3] + s[i+1:]
    return s

def add(s1,s2):
    s = reduce([-1] + s1 + s2 + [-3])
    snail_to_string(s)
    return s

def reduce(s):
    depth = 0
    l = -1
    r = -1
    for i in range(len(s)):
        if s[i] < 0:
            depth += s[i] + 2
        else:
            if depth > 4 and s[i+1] >= 0:
                r = i + 2
                while s[r] < 0:
                    r += 1
                    if r >= len(s):
                        r = -1
                        break
                s = explode(s,l,i,i+1,r)
                snail_to_string(s)
                return reduce(s)
            l = i
    depth = 0
    for i in range(len(s)):
        if s[i] >= 10:
            s = split(s,i)
            snail_to_string(s)
            return reduce(s)
    return s

def snail_to_string(s):
    output = ""
    for i in range(len(s)):
        if s[i] == -1:
            output += '['
        elif s[i] == -3:
            if i < len(s)-1 and s[i+1] != -3:
                output += '],'
            else:
                output += ']'
        else:
            if s[i+1] >= -1:
                output += str(s[i]) + ','
            else:
                output += str(s[i])
    return output

def convert_to_snail(s):
    o = []
    for c in s:
        if c == '[':
            o.append(-1)
        elif c == ']':
            o.append(-3)
        elif c != ',':
            o.append(int(c))
    return o

def get_pairs(s):
    if s[1] >= 0:
        return [[s[1]],s[2:-1]]
    elif s[-2] >= 0:
        return [s[1:-2],[s[-2]]]
    depth = 0
    for i in range(len(s)):
        if s[i] == -3:
            if depth == 2:
                return [s[1:i+1],s[i+1:-1]]
            else:
                depth -= 1
        elif s[i] == -1:
            depth += 1

def magnitude(s):
    if len(s) == 1:
        return s[0]
    l,r = get_pairs(s)
    return (3 * magnitude(l)) + (2 * magnitude(r))

def main():
    f = open("input","r")
    lines = f.readlines()
    f.close()
    
    s = add(convert_to_snail(lines[0].strip()),convert_to_snail(lines[1].strip()))

    for i in range(2,len(lines)):
        if lines[i] == '\n':
            break
        s = add(s,convert_to_snail(lines[i].strip()))
    
    print(magnitude(s))


if __name__ == "__main__":
    main()

