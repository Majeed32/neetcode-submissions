class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]*(len(s)+1) 
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != "0" else 0
        n = len(s)   
        for i in range(n-2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif int(s[i : i+2]) > 26:
                dp[i] = dp[i+ 1]
            else:
                dp[i] = dp[i+1] + dp[i+2]
        return dp[0]