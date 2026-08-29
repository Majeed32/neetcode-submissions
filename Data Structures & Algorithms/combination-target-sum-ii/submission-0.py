class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start, stack, target):
            if target == 0:
                res.append(stack[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                stack.append(candidates[i])
                dfs(i+1, stack, target - candidates[i])
                stack.pop()
        dfs(0, [], target)
        return res

        