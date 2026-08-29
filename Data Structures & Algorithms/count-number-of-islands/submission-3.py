class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r,c):
            grid[r][c] = '0'
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    dfs(nr, nc)
        res = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    res += 1
                    dfs(row, col)
        return res
