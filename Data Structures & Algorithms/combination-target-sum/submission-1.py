class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, stack, curr_sum):
            if curr_sum == target:
                res.append(stack[:])
                return
            if curr_sum > target or i == len(nums):
                return
            stack.append(nums[i])
            dfs(i, stack, curr_sum+nums[i])
            stack.pop()
            dfs(i+1, stack, curr_sum)
        dfs(0, [], 0)
        return res

        