class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, stack, currSum):
            if currSum == target:
                res.append(stack[:])
                return
            if i >= len(nums) or currSum > target:
                return
            stack.append(nums[i])
            dfs(i, stack, currSum + nums[i])
            stack.pop()
            dfs(i+1, stack, currSum)
        dfs(0, [], 0)
        return res
        