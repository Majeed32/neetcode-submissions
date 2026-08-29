class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            temp = max(num+a, b)
            a = b
            b = temp
        return b