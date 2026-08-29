class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        safe = set()
        def dfs(r, c):
            if board[r][c] == 'X':
                return
            safe.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if (nr, nc) not in safe and board[nr][nc] == 'O':
                        dfs(nr, nc)
        for r in range(m):
            dfs(r, 0)
            dfs(r, n-1)
        for c in range(n):
            dfs(0, c)
            dfs(m-1, c)
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O' and (row, col) not in safe:
                    board[row][col] = 'X'
        
        