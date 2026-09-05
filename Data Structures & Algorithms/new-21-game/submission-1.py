class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k-1+maxPts:
            return 1.0
        size = k+maxPts
        dp = [0.0]*size
        for i in range(k, min(n, size-1)+1):
            dp[i] = 1.0
        window = sum(dp[k: k+maxPts])
        for j in range(k-1, -1, -1):
            dp[j] = window/maxPts
            window += dp[j] - dp[j+maxPts]
        return dp[0]
        # dp = [0]*(n+1)
        # dp[0] = 1
        # s = 1 if k > 0 else 0
        # for i in range(1, n+1):
        #     dp[i] = s / maxPts
        #     if i < k:
        #         s += dp[i]
        #     # for j in range(1, maxPts+1):
        #     if i-maxPts >= 0 and i-j < k:
        #         dp[i] += dp[i-j]/maxPts
        return sum(dp[k:])
        