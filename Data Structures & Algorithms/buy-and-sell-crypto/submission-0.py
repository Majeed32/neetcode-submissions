class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallestSoFar = prices[0]
        for price in prices:
            if price < smallestSoFar:
                smallestSoFar = price
            profit = max(profit, price - smallestSoFar)
        return profit

        