class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        heap = [(0,k)]
        seen = set()
        time = 0
        while heap:
            t, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            if len(seen) == n:
                return t
            for nei, new_t in graph[node]:
                heapq.heappush(heap, (new_t+t, nei))
        return -1


        