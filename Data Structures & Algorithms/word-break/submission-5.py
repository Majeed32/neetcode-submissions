class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        word_dict = set(wordDict)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i+1):
                if s[j: i+1] in word_dict and dp[j]:
                    dp[i+1] = True
        return dp[-1]



        