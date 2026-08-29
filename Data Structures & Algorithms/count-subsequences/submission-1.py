class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[n][i] = 1
        for r in range(n-1, -1, -1):
            for c in range(m-1, -1, -1):
                if t[r] == s[c]:
                    dp[r][c] = dp[r+1][c+1] + dp[r][c+1]
                else:
                    dp[r][c] = dp[r][c+1]
        return dp[0][0]
        