class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, stack):
            if i >= len(nums):
                res.append(stack[:])
                return
            dfs(i + 1, stack + [nums[i]])
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, stack)
        dfs(0, [])
        return res
        