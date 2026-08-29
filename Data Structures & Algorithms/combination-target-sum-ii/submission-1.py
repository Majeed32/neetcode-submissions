class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, stack, target):
            if target == 0:
                res.append(stack[:])
                return
            if target < 0 or i >= len(candidates):
                return
            stack.append(candidates[i])
            dfs(i+1, stack, target - candidates[i])
            stack.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, stack, target)
        dfs(0, [], target)
        return res

        