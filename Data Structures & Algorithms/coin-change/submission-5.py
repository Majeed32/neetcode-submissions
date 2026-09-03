class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        for target in range(1, amount+1):
            for coin in coins:
                rem = target - coin
                if rem >= 0 and dp[rem] + 1 < dp[target]:
                    dp[target] = dp[rem] + 1
        return dp[-1] if dp[-1] != math.inf else -1
        