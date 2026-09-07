class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for prev, count in dp.items():
                next_dp[prev+num] += count
                next_dp[prev-num] += count
            dp = next_dp
        return dp[target]
        