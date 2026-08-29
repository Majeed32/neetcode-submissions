class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(graph, src, visited):
            if src in visited:
                return False
            visited.add(src)
            for neighbor in graph[src]:
                dfs(graph, neighbor, visited)
            return True
        visited = set()
        for i in range(n):
            if i not in graph or dfs(graph, i, visited):
                count += 1
        return count 


        