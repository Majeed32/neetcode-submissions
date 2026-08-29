class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0
        while l < r: 
            if heights[l] < heights[r]:
                area = heights[l] * (r-l)
                l += 1
            else:
                area  = heights[r] * (r-l)
                r -= 1
            res = max(res, area)
        return res
        