class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, stack, curr_sum):
            if curr_sum == target:
                res.append(stack[:])
                return
            if i >= len(candidates) or curr_sum > target:
                return
            dfs(i + 1, stack + [candidates[i]], curr_sum + candidates[i])
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, stack, curr_sum)
        dfs(0, [], 0)
        return res
        