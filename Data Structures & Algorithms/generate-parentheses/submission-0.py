class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open_count, close_count, curr):
            if open_count == 0 and close_count == 0:
                res.append(curr)
                return
            if close_count > open_count:
                dfs(open_count, close_count - 1, curr + ")")
            if open_count > 0:
                dfs(open_count -1, close_count, curr + "(")
        dfs(n, n, "")
        return res