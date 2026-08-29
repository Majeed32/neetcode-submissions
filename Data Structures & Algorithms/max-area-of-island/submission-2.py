class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r: int, c: int) -> int:
            if not grid[r][c]:
                return 0
            grid[r][c] = 0
            size = 1
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    size += dfs(nr, nc)
            return size
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    res = max(res, dfs(row, col))
        return res

        