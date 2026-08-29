class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        edges = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                edges.append([i, j, dist])
        edges.sort(key = lambda x : x[2])
        res = 0
        for i, j, dist in edges:
            if uf.union(i,j):
                res += dist
        return res


        