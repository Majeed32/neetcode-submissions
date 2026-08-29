class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c):
            if (r, c) in seen:
                return
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1":
                    dfs(nr, nc)
        res = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs(row, col)
                    res += 1
        return res
                    
                


            
        