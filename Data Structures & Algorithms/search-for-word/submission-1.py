class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        def dfs(i, r, c):
            if i == len(word)-1:
                return board[r][c] == word[i]
            if board[r][c] != word[i]:
                return False
            visited.add((r,c))
            for dr, dc in directions:
                nr,nc = r+dr, c+dc
                if 0 <= nr< m and 0 <= nc < n and (nr, nc) not in visited:
                    if dfs(i+1, nr, nc):
                        return True
            visited.remove((r,c))
            return False
        for row in range(m):
            for col in range(n):
                if dfs(0, row, col):
                    return True
        return False
            
        