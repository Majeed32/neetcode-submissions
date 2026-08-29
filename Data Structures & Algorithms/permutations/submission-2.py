class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        seen = set()
        def dfs(i, stack):
            if i == n:
                res.append(stack[:])
            for j in range(len(nums)):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    stack.append(nums[j])
                    dfs(i + 1, stack)
                    seen.discard(nums[j])
                    stack.pop()
        dfs(0, [])
        return res
        