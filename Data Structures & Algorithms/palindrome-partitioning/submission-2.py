class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def dfs(i, stack):
            if i == len(s):
                res.append(stack.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    dfs(j+1, stack + [s[i : j+1]])
        dfs(0, [])
        return res

        