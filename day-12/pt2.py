import copy
import itertools

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
        visited = [0] * self.length
        path = []
        paths = []

        for i in range(self.length):
            if (self.big[i] or i == self.str_to_id[src] or i == self.str_to_id[tgt]):
                continue
            self.all_paths_recursive(self.str_to_id[src],self.str_to_id[tgt],visited,path,paths,i)


        return paths

    def all_paths_recursive(self, src_id, tgt_id, visited, path, paths,spec):
        visited[src_id] += 1
        path.append(src_id)

        if src_id == tgt_id:
            newpath = copy.deepcopy(path)
            #if newpath not in paths:
            paths.append(newpath)
        else:
            for i in self.adj[src_id]:
                if visited[i] == 0 or self.big[i] or (i == spec and visited[spec] < 2):
                    self.all_paths_recursive(i, tgt_id, visited, path, paths,spec)

        path.pop()
        visited[src_id] -= 1

g = Graph(lines)
paths = g.all_paths("start","end")

paths.sort()

print(len(list(paths for paths,_ in itertools.groupby(paths))))

