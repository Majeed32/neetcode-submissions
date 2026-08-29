class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = [["."]*n for _ in range(n)]
        res = []
        visited = set()
        diag1 = set()
        diag2 = set()
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in state])
                return
            for c in range(n):
                if c not in visited and r-c not in diag1 and r+c not in diag2:
                    visited.add(c)
                    diag1.add(r-c)
                    diag2.add(r+c)
                    state[r][c] = "Q"
                    dfs(r+1)
                    visited.discard(c)
                    diag1.discard(r-c)
                    diag2.discard(r+c)
                    state[r][c] = "."
        dfs(0)
        return res
        