class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for curr in range(1, target+1):
            for num in nums:
                rem  = curr-num
                if rem >= 0:
                    dp[curr] += dp[rem]
        return dp[target]
        