class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r, c):
            if not (0 <= r < m) or not (0 <= c < n) or board[r][c] != "O":
                return 
            board[r][c] = "M"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        for i in range(m):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][n-1] == "O":
                dfs(i, n-1)
        for j in range(n):
            if board[0][j] == "O":
                dfs(0,j)
            if board[m-1][j] == "O":
                dfs(m-1, j)
        for row in range(m):
            for col in range(n):
                if board[row][col] == "M":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col]  = "X"
        
