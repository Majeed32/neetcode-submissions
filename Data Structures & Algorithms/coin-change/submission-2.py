class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                subAmount = i - coin
                if subAmount >= 0:
                    dp[i] = min(dp[i], 1 + dp[subAmount])
        return dp[amount] if dp[amount] != float("inf") else -1