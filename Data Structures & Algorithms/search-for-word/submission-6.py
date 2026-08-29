class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        seen = set()
        def dfs(i, r, c):
            if i == len(word)-1:
                return board[r][c] == word[i]
            if word[i] != board[r][c]:
                return False
            seen.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    if dfs(i+1, nr, nc):
                        return True
            seen.discard((r, c))
            return False
        for r in range(m):
            for c in range(n):
                if dfs(0, r, c):
                    return True
        return False


        