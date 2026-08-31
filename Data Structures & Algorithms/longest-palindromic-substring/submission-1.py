class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(word):
            return word == word[: :-1]
        dp = [1]* len(s)
        curr_max = 1
        ans = (0, 1)
        for i in range(len(s)):
            for j in range(i):
                if is_palindrome(s[j: i+1]):
                    dp[i] = max(dp[i], i - j + 1)
                    if dp[i] > curr_max:
                        ans = (j, i+1)
                        curr_max = dp[i]
        l,r  = ans
        return s[l : r]
        