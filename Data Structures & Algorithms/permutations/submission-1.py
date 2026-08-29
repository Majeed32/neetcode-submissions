class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(stack, seen):
            if len(stack) == n:
                res.append(stack[:])
            for j in range(len(nums)):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    stack.append(nums[j])
                    dfs(stack, seen)
                    seen.discard(nums[j])
                    stack.pop()
        dfs([], set())
        return res
        