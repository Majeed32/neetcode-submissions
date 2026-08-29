class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(m, n, memo):
            if m == 0 or n == 0:
                return 0
            if (m, n) in memo:
                return memo[(m, n)]
            if text1[m-1] == text2[n-1]:
                res = 1 + lcs(m-1, n-1, memo)
            else:
                res = max(lcs(m-1, n, memo), lcs(m, n-1, memo))
            memo[(m, n)] = res
            return res
        return lcs(len(text1), len(text2), {})
        