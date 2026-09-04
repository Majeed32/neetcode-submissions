class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(len(days)+1)
        for idx, d in enumerate(days):
            
            if idx == 0:
                dp[idx+1] = min(costs)
                continue
            curr_min = math.inf
            curr_min = min(curr_min, dp[idx] + costs[0])

            prev = idx - 1
            while prev >= 0 and days[prev] > d - 7:
                prev  -= 1
            if prev >= 0:
                curr_min = min(curr_min, dp[prev+1] + costs[1])
            else:
                curr_min = min(curr_min, costs[1])

            prev = idx - 1
            while prev >= 0 and days[prev] > d - 30:
                prev  -= 1
            if prev >= 0:
                curr_min = min(curr_min, dp[prev+1] + costs[2])
            else:
                curr_min = min(curr_min, costs[2])

            dp[idx+1] = curr_min
            
        return dp[-1]
        