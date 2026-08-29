class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, stack):
            res.append(stack[:])
            for i in range(start, len(nums)):
                stack.append(nums[i])
                backtrack(i+1, stack)
                stack.pop()
        backtrack(0, [])
        return res
        