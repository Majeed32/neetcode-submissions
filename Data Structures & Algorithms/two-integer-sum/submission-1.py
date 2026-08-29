class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if nums[i] in my_dict:
                return [my_dict[nums[i]], i]
            my_dict[remainder] = i
        return []

        