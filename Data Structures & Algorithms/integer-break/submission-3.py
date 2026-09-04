class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1) 
        for i in range(2, n+1):
            for j in range(1, i):
                rem = i-j
                dp[i] = max(dp[i], dp[rem]* j, rem *j)
        return dp[-1]

        