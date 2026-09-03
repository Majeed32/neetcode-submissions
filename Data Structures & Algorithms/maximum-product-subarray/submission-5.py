class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = -math.inf
        curr_max, curr_min = 1, 1
        for n in nums:
            prev_max, prev_min = curr_max, curr_min
            curr_max = max(prev_max * n, prev_min*n, n)
            curr_min = min(prev_min * n, n, prev_max*n)
            global_max = max(global_max, curr_max)
        return global_max
        
        