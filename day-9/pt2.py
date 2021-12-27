f = open("input","r")
unformatted_lines = f.readlines()
f.close()

# board must be at least 2x2

xlen = len(unformatted_lines[0]) - 1
ylen = len(unformatted_lines)

board = []

def get_neighbors(i,j,board): 
    # takes in coordinates and a board, returns array of triples 
    # containing coordinates to a neighbor and the neighbor's value

    # i is row, j is column

    output = []

    xlen = len(board[0])
    ylen = len(board)

    if i == 0:
        if j == 0:
            output.append([0,1])
            output.append([1,0])
            return output
        if j == xlen - 1:
            output.append([0,j-1])
            output.append([1,j])
            return output
        else:
            output.append([0,j+1])
            output.append([0,j-1])
            output.append([1,j])
            return output
    elif i == ylen - 1:
        if j == 0:
            output.append([i,1])
            output.append([i-1,0])
            return output
        elif j == xlen - 1:
            output.append([i,j-1])
            output.append([i-1,j])
            return output
        else:
            output.append([i,j-1])
            output.append([i,j+1])
            output.append([i-1,j])
            return output
    else:
        if j == 0:
            output.append([i,1])
            output.append([i-1,0])
            output.append([i+1,0])
            return output
        elif j == xlen - 1:
            output.append([i,j-1])
            output.append([i-1,j])
            output.append([i+1,j])
            return output
        else:
            output.append([i-1,j])
            output.append([i+1,j])
            output.append([i,j-1])
            output.append([i,j+1])
            return output


for line in unformatted_lines:
    board.append(list(map(int,list(line.strip()))))

output = 0

lowpts = []

for i in range(len(board)):
    for j in range(len(board[0])):
        lowpt = True
        for n in get_neighbors(i,j,board):
            if board[i][j] >= board[n[0]][n[1]]:
                lowpt = False
                break
        if lowpt:
            output += 1 + board[i][j]
            lowpts.append([i,j])

basins = []

for l in lowpts:
    q = [l]
    basin = []
    done = []

    while len(q) > 0:
        n = q.pop()
        if n in done:
            continue
        done.append(n)
        if board[n[0]][n[1]] != 9:
            basin.append(n)
            for m in get_neighbors(n[0],n[1],board):
                if (m not in done):
                    q.append(m)

    basins.append(len(basin))

basins.sort(reverse=True)

print(basins[0] * basins[1] * basins[2])