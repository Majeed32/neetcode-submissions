class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if nums[i] in myDict:
                return [myDict[nums[i]], i]
            myDict[remainder] = i