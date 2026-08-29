class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(res)):
            res[i] *= prefix
            prefix *= nums[i]
        suffix = 1
        for j in range(len(res)-1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        return res
        