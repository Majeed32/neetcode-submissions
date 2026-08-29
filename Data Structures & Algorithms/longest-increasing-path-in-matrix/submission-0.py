class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        m, n = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def lip(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            temp = 1
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr < m and nr >= 0 and nc < n and nc >= 0 and matrix[nr][nc] > matrix[r][c]:
                    temp = max(temp, 1 + lip(nr, nc))
            memo[(r,c)] = temp
            return temp
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, lip(i, j))
        return res


        