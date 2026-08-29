class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False
        self.word = ""
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.end_of_word = True
        curr.word = word
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r: int, c: int, curr: TrieNode) -> Optional[str]:
            char = board[r][c]
            idx = ord(char) - ord('a')
            curr = curr.children[idx]
            if not curr:
                return
            if curr.end_of_word:
                ans.add(curr.word)
            board[r][c] = "#"
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    dfs(nr, nc, curr)
            board[r][c] = char
        for word in words:
            self.add_word(word)
        ans = set()
        curr = self.root
        for row in range(m):
            for col in range(n):
                dfs(row, col, curr)
        return list(ans)




        