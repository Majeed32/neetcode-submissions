class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        pal_len, pal_idx = 0, -1
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i + 1 > pal_len:
                        pal_len = j-i+1
                        pal_idx = i
        return s[pal_idx : pal_idx+pal_len]
        