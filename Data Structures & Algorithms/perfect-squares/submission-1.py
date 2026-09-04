class Solution:
    def numSquares(self, n: int) -> int:
        num_list = []
        start = 1
        square = 1
        while square <= n:
            num_list.append(square)
            start += 1
            square = start*start
        dp = [math.inf]*(n+1)
        dp[0] = 0
        for target in range(1, n+1):
            for num in num_list:
                rem = target-num
                if rem >= 0:
                    dp[target] = min(dp[target], dp[rem]+1)
        return dp[n]


        