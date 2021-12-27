import copy

f = open("input","r")
lines = f.readlines()
f.close()

class Graph:
    def __init__(self, edgelist):
        self.str_to_id = {} # dictionary<string,int>    string to id (int)
        self.id_to_str = [] # list<string>              id (int) to string
        self.adj = []       # list<set>                 adjacency list
        self.big = []       # list<bool>                stores whether id is big or small
        self.length = 0     # int                       number of nodes

        for edge in edgelist:
            if '-' not in edge:
                break

            src = edge.strip().split('-')[0]
            tgt = edge.strip().split('-')[1]

            if src not in self.str_to_id:
                self.str_to_id[src] = self.length
                self.id_to_str.append(src)
                self.adj.append(set({}))
                self.big.append(src.isupper())
                self.length += 1

            if tgt not in self.str_to_id:
                self.str_to_id[tgt] = self.length
                self.id_to_str.append(tgt)
                self.adj.append(set({}))
                self.big.append(tgt.isupper())
                self.length += 1

            src_id = self.str_to_id[src]
            tgt_id = self.str_to_id[tgt]
            
            self.adj[src_id].add(tgt_id)
            self.adj[tgt_id].add(src_id)

    def all_paths(self, src, tgt):
        visited = [False] * self.length
        path = []
        paths = []
        self.all_paths_recursive(self.str_to_id[src],self.str_to_id[tgt],visited,path,paths)
        return paths

    def all_paths_recursive(self, src_id, tgt_id, visited, path, paths):
        if not self.big[src_id]:
            visited[src_id] = True
        path.append(src_id)

        if src_id == tgt_id:
            paths.append(copy.deepcopy(path))
        else:
            for i in self.adj[src_id]:
                if not visited[i]:
                    self.all_paths_recursive(i, tgt_id, visited, path, paths)

        path.pop()
        visited[src_id] = False

g = Graph(lines)
paths = g.all_paths("start","end")
for path in paths:
    print(path)

print(len(paths))

