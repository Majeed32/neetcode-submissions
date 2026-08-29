class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        def dfs(i):
            if i >= len(s):
                res.append(stack[:])
                return
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    stack.append(s[i : j+1])
                    dfs(j+1)
                    stack.pop()
        dfs(0)
        return res

        