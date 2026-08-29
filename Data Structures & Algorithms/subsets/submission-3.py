class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, stack):
            if i == len(nums):
                res.append(stack[:])
                return
            dfs(i+1, stack + [nums[i]])
            dfs(i+1, stack)
        dfs(0, [])
        return res
        