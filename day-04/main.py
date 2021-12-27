f = open("input","r")
lines = f.readlines()
f.close()

boards = []

for i in range(len(lines)):
    if i == 0:
        continue

    if lines[i] == "\n":
        boards.append([])
        for j in range(5):
            boards[len(boards)-1].append(list(map(int,lines[i+j+1].split())))
        for j in range(5):
            b = []
            for k in range(5):
                b.append(boards[len(boards)-1][k][j])
            boards[len(boards)-1].append(b)

nums = list(map(int,lines[0].split(',')))

count = [0,0]

for i in range(len(boards)):
    winning_num = 10000
    for row in boards[i]:
        total_found = 0
        for j in range(len(nums)):
            if nums[j] in row:
                total_found += 1
            if total_found == 5:
                if i == 1:
                    print(row)
                    print(j)
                if j < winning_num:
                    print('---')
                    print(i,j)
                    print('---')
                    winning_num = j
                break
    if winning_num > count[1]:
        count[0] = i
        count[1] = winning_num


print()
print()
print()
print(count)

print(nums)
nums = nums[:count[1] + 1]


score = 0

for i in range(5):
    for n in boards[count[0]][i]:
        if n not in nums:
            score += n

score *= nums[count[1]]

print(score)
        
        







