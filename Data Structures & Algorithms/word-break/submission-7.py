class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        word_dict = set(wordDict)
        dp[0] = True
        for i in range(len(s)):
            for word in word_dict:
                n = len(word)
                if i - n + 1 >= 0:
                    if s[i-n+1: i+1] == word and dp[i - n+1]:
                        dp[i+1] = True
        return dp[-1]



        