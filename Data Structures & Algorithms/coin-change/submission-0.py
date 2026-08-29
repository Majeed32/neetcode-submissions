class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(target):
            if target in memo:
                return memo[target]
            if target == 0:
                return 0
            if target < 0:
                return -1
            minCoins = -1
            for coin in coins:
                subAmount = target - coin
                res = dp(subAmount)
                if res > -1:
                    res += 1
                    if minCoins == -1 or res < minCoins:
                        minCoins = res
            memo[target] = minCoins
            return minCoins
        return dp(amount)

        