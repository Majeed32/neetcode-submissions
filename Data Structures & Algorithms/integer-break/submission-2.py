class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 2:
            return 0
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 0
        if n == 2:
            return 1
        dp[2] = 1
        
        for i in range(2, n+1):
            for j in range(1, i):
                rem = i-j
                dp[i] = max(dp[i], dp[rem]* j, rem *j)
        print(dp)
        # dp[0] = [0, 0]
        # dp[1] = [1, 0]
        # if n == 2:
        #     return 1
        # dp[2] = [2, 1]
        # for j in range(2, n+1):
        #     if not j % 2:
        #         max_sum = dp[j//2][0]* 2
        #         max_product = dp[j//2][0] * dp[j//2][0]
        #         dp[j] = [max_sum, max_product]
        #     else:
        #         new = dp[j//2]
        #         t = dp[j//2 + 1]
        #         max_sum = new[0] + t[0]
        #         max_product = new[0]*t[0]
        #         dp[j] = [max_sum, max_product]
        # print(dp)
        return dp[-1]

        