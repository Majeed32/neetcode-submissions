class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_possible(num):
            total = 0
            for p in piles:
                total += ((p // num) if not p% num else (p//num) + 1)
            return total <= h
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l)//2
            if is_possible(m):
                r = m
            else:
                l = m+1
        return r
        