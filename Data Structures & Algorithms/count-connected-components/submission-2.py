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
        for key in graph:
            if dfs(graph, key, visited):
                count += 1
        return count if graph else n


        