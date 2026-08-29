class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = float('-inf')
        localMax = 0
        for num in nums:
            localMax = max(localMax + num, num)
            if localMax > globalMax:
                globalMax = localMax
        return globalMax


        