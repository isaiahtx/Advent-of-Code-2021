f = open("input","r")
lines = f.readlines()
f.close()

scores = {
    "(" : 1,
    "[" : 2,
    "{" : 3,
    "<" : 4
}

opening = ['(','[','{','<']
closing = [')',']','}','>']

open_to_close = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

final_scores = []

for line in lines:
    score = 0
    q = []
    valid = True
    for i in range(len(line)):
        if line[i] in opening:
            q.append(line[i])
        elif line[i] in closing:
            removed = q.pop()
            if (open_to_close[removed] != line[i]):
                #print("Expected",open_to_close[removed],end=", ")
                #print("but found",line[i],"instead")
                valid = False
                break
        else:
            break

    if valid:
        while (len(q) > 0):
            score *= 5
            score += scores[q.pop()]
        final_scores.append(score)

final_scores.sort()
print(final_scores[int(len(final_scores) / 2)])
            