class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m  = len(grid), len(grid[0])
        seen = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r, c):
            if (r, c) in seen:
                return 0
            seen.add((r, c))
            size = 1
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc]:
                    size += dfs(nr, nc)
            return size
        res = 0
        for row in range(n):
            for col in range(m):
                if (row, col) not in seen and grid[row][col]:
                    res = max(res, dfs(row, col))
        return res

        