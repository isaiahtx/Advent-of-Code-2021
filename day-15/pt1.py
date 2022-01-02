import math

f = open("input","r")
lines = f.readlines()
f.close()

board = []

for line in lines:
    board.append(list(map(int,list(line.strip()))))

def encode(x,y,board):
    return (x * len(board[0])) + y

def decode(x,board):
    return [math.floor(x / len(board[0])),x % len(board[0])]

def neighbors(row,col,board):
    moves = []
    for i in [[0,1],[0,-1],[1,0],[-1,0]]:
        temp_row = row + i[0]
        temp_col = col + i[1]

        if (0 <= temp_row < len(board)) and (0 <= temp_col < len(board[0])):
            moves.append([temp_row,temp_col])

    return moves

class priority_queue():
    def __init__(self,board):
        self.size = 0
        self.d = dict({})
        self.b = board

    def push(self,cell,dist):
        x = encode(cell[0],cell[1],self.b)
        if x not in self.d.keys():
            self.size += 1
        self.d[x]=dist

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        x = min(self.d, key=self.d.get)
        y = self.d[x]
        del self.d[x]
        z = decode(x,self.b)
        return [z[0],z[1],y]

def pb(board):
    for r in board:
        for el in r:
            if el == None:
                print('N',end=' ')
            else:
                print(el,end=' ')
        print()

def dijkstra(board,src):
    pq = priority_queue(board)
    dist = []

    for i in range(len(board)):
        dist.append([float('inf')] * len(board[0]))
        for j in range(len(board[0])):
            if [i,j] == src:
                pq.push(src,0)
            else:
                pq.push([i,j],float('inf'))
    
    dist[src[0]][src[1]] = 0

    while pq.size > 0:
        u = pq.pop()
        for v in neighbors(u[0],u[1],board):
            alt = dist[u[0]][u[1]] + board[v[0]][v[1]]
            if alt < dist[v[0]][v[1]]:
                dist[v[0]][v[1]] = alt
                pq.push(v,alt)

    return dist

pair = dijkstra(board,[0,0])

print(pair[-1][-1])

