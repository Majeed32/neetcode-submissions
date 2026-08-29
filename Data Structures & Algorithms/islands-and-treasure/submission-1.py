class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        queue = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        while queue:
            r, c, dist = queue.popleft()
            grid[r][c] = dist
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr >= 0 and nr < m and nc >= 0 and nc < n:
                    if (nr, nc) not in visited and grid[nr][nc] != -1:
                        queue.append((nr, nc, dist+1))
                        visited.add((nr,nc))

        