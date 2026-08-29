class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(target):
            if target in memo:
                return memo[target]
            if target == 0:
                return 0
            if target < 0:
                return float("inf")
            minCoins = float("inf")
            for coin in coins:
                subAmount = target - coin
                res = dp(subAmount)
                if res != float("inf"):
                    minCoins = min(minCoins, res+1)
            memo[target] = minCoins
            return minCoins
        res = dp(amount)
        return res if res != float("inf") else -1

        