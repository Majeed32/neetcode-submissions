class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = math.inf
        res = 0
        for p in prices:
            min_so_far = min(min_so_far, p)
            res = max(res, p - min_so_far)
        return res
        