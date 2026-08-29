class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        queue = deque()
        seen = set()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    seen.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        if not fresh:
            return 0
        t = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if (nr, nc) not in seen and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr, nc))
                            seen.add((nr, nc))
            t += 1
        return t if not fresh else -1

        