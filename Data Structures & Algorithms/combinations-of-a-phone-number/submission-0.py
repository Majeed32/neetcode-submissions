class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if not digits:
            return res
        def dfs(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            if i >= len(digits):
                return 
            for char in phoneMap[digits[i]]:
                dfs(i+1, curr + char)
        dfs(0, "")
        return res
        