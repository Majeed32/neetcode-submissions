class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(k):
            hours = 0
            for pile in piles:
                if pile % k == 0:
                    hours += (pile // k)
                else:
                    hours += (pile // k) + 1
            return hours <= h
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left)//2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        