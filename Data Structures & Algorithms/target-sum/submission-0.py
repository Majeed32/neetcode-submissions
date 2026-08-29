class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(i, count):
            if i == len(nums):
                return 1 if count == target else 0
            if (i, count) in memo:
                return memo[(i, count)]
            res = backtrack(i+1, count + nums[i]) + backtrack(i+1, count-nums[i])
            memo[(i, count)] = res
            return res
        return backtrack(0, 0)
        