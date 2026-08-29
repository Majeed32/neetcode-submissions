class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0 
        for idx, num in enumerate(nums):
            if idx > reach:
                return False
            reach = max(reach, idx+num)
        return True
        