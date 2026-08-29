class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(i, stack):
            if i == len(nums):
                res.append(stack[:])
                return
            for j in range(len(nums)):
                if j not in visited:
                    visited.add(j)
                    stack.append(nums[j])
                    dfs(i+1, stack)
                    stack.pop()
                    visited.remove(j) 
        dfs(0, [])
        return res