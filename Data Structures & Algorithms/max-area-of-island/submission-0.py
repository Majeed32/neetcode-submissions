class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [1,0], [-1, 0], [0,-1]]
        def dfs(grid, row, col, visited):
            rowBounds = 0 <= row < m
            colBounds = 0 <= col < n
            if not rowBounds or not colBounds:
                return 0
            if grid[row][col] == 0:
                return 0
            if visited[row][col]:
                return 0
            visited[row][col] = True
            size = 1
            for x, y in directions:
                size += dfs(grid, row + x, col + y, visited)
            return size
        res = 0
        visited = [[False]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                val = dfs(grid, row, col, visited)
                res = max(res, val)
        return res
        
        
        