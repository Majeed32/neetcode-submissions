class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(heights) - 1
        while left < right:
            curr_height = min(heights[left], heights[right])
            area = (right - left) * curr_height
            maxWater = max(maxWater, area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxWater
        