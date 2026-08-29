class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pacific_set, atlantic_set = set(), set()
        def dfs(r, c, seen):
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, seen)
        for r in range(m):
            dfs(r, 0, pacific_set)
            dfs(r, n-1, atlantic_set)
        for c in range(n):
            dfs(0, c, pacific_set)
            dfs(m-1, c, atlantic_set)
        intersect = pacific_set & atlantic_set
        return list(intersect)


        