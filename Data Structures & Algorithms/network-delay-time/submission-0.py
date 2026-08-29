class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        visited = set()
        for u, v, t in times:
            adjList[u].append((v, t))
        heap = [(0, k)]
        res = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, time)
            print(res, node)
            for neighbor, t in adjList[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (t+time, neighbor))
        return res if len(visited) == n else -1
        
        