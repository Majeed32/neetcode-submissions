class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target //= 2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for rem in range(target, num-1, -1):
                if dp[rem-num]:
                    dp[rem] = True
        return dp[target]
        