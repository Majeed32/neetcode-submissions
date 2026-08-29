class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        queue = deque()
        seen = set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    seen.add((row, col))
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c  = queue.popleft()
                if grid[r][c] == -1:
                    continue
                if grid[r][c]:
                    grid[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if (nr, nc) not in seen:
                            queue.append((nr, nc))
                            seen.add((nr, nc))
            dist += 1
        