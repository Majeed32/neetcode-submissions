class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(grid, row, col, visited):
            if not (0 <= row < m) or not(0 <= col < n):
                return False
            if grid[row][col] == "0":
                return False
            if (row, col) in visited:
                return False
            visited.add((row, col))
            for x, y in directions:
                dfs(grid, row + x, col + y, visited)
            return True

        res = 0
        for row in range(m):
            for col in range(n):
                if dfs(grid, row, col, visited):
                    res += 1
        return res

        