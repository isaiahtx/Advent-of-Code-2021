f = open("input","r")
lines = f.readlines()
f.close()

flashes = 0

def get_neighbors(i,j): 
    output = []
    for os in [[1,0],[1,1],[0,1],[-1,0],[-1,-1],[0,-1],[1,-1],[-1,1]]: # 'os' for 'offset'
        if (0 <= (i + os[0]) <= 9) and (0 <= (j + os[1]) <= 9): # it's cursed that python lets you do this
            output.append([i+os[0],j+os[1]])
    return output

def update_board(board):
    q = []

    for i in range(10):
        for j in range(10):
            board[i][j] += 1
            if board[i][j] > 9:
                board[i][j] = 0
                for n in get_neighbors(i,j):
                    q.append(n)
    
    while len(q) > 0:
        o = q.pop()
        i = o[0]
        j = o[1]
        if board[i][j] == 0:
            continue
        board[i][j] += 1
        if board[i][j] > 9:
            board[i][j] = 0
            for n in get_neighbors(i,j):
                q.append(n)

    flashes = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                flashes += 1

    return flashes

board = []

for line in lines:
    board.append(list(map(int,list(line.strip()))))

#for row in board:
    #for el in row:
        #print(el,end="")
    #print()

count = int(input())
flashes = 0

for i in range(count):
    flashes += update_board(board)

for row in board:
    for el in row:
        print(el,end="")
    print()

print()
print(flashes)

