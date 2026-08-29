class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = float("-inf")
        curr_max, curr_min = 1, 1
        for num in nums:
            prev_max, prev_min = curr_max, curr_min
            curr_max = max(prev_max*num,prev_min*num, num)
            curr_min = min(prev_max*num,prev_min*num, num)
            global_max = max(global_max, curr_max)
        return global_max
