class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        heap = [[grid[0][0], 0, 0]]
        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            if (r, c) == (m-1, n-1):
                return time
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    n_time = max(time, grid[nr][nc])
                    heapq.heappush(heap, (n_time, nr, nc))
        return -1
        