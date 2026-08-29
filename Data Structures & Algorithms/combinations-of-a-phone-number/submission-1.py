class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combination_map = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        res = []
        def dfs(i, stack):
            if i >= len(digits):
                if stack:
                    res.append("".join(stack))
                return
            for char in combination_map[digits[i]]:
                dfs(i + 1, stack + [char])
        dfs(0, [])
        return res
        