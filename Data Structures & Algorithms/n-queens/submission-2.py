class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']* n for _ in range(n)]
        col_seen = set()
        pos_diag, neg_diag = set(), set()
        res = []
        def dfs(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return
            for j in range(n):
                if j not in col_seen and (i+j) not in pos_diag and (i-j) not in neg_diag:
                    col_seen.add(j)
                    pos_diag.add(i+j)
                    neg_diag.add(i-j)
                    board[i][j] = "Q"
                    dfs(i+1)
                    board[i][j] = "."
                    col_seen.discard(j)
                    pos_diag.discard(i+j)
                    neg_diag.discard(i-j)
        dfs(0)
        return res

