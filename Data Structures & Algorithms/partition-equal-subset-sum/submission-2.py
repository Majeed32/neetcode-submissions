class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for rem in range(target//2, num-1, -1):
                if dp[rem-num]:
                    dp[rem] = True
        return dp[target//2]
        