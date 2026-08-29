class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r  = 0, len(height)-1
        left_max, right_max = 0, 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            min_max = min(left_max, right_max)
            if height[l] < height[r]:
                res = max(res, res + min_max - height[l])
                l += 1
            else:
                res = max(res, res + min_max - height[r])
                r -= 1
        return res
        