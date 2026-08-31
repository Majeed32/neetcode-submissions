class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def check(curr):
            prev1, prev2 = 0, 0
            for num in curr:
                nxt  = max(num + prev1, prev2)
                prev1 = prev2
                prev2 = nxt
            return prev2
        return max(check(nums[ : -1]), check(nums[1:]))
        