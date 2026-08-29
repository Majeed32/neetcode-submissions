class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.count = n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] >= self.rank[root_y]:
            self.rank[root_x] += self.rank[root_y]
            self.parent[root_y] = root_x
        else:
            self.rank[root_y] += self.rank[root_x]
            self.parent[root_x] = root_y
        self.count -= 1
        return True
    
    def component_count(self):
        return self.count
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.component_count()
        