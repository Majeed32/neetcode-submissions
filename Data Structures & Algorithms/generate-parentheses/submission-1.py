class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(open, close, stack):
            if open == 0 and close == 0:
                res.append("".join(stack))
                return
            if open < 0 or close < 0:
                return
            if open <= close:
                dfs(open-1, close, stack + ["("])
                dfs(open, close-1, stack + [")"])
            if close < open:
                return
        dfs(n, n, [])
        return res
        