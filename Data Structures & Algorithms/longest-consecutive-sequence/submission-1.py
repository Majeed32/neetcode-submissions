class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for n in num_set:
            if n-1 not in num_set:
                curr, curr_num = 0, n
                while curr_num in num_set:
                    curr += 1
                    curr_num += 1
                res = max(res, curr)
        return res

        