class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(len(days)+1)
        for idx, d in enumerate(days):
            
            if idx == 0:
                dp[idx+1] = min(costs)
                continue
            curr_min = math.inf
            curr_min = min(curr_min, dp[idx] + costs[0])
            # print(idx, dp,curr_min)
            if d - 7 >= 0:
                prev = idx - 1
                while prev >= 0 and days[prev] > d - 7:
                    prev  -= 1
                curr_min = min(curr_min, dp[prev+1] + costs[1])
            else:
                curr_min = min(curr_min, costs[1])
            # print(idx, dp,curr_min)
            if d - 30 >= 0:
                prev = idx - 1
                while prev >= 0 and days[prev] > d - 30:
                    prev  -= 1
                if prev >= 0:
                    curr_min = min(curr_min, dp[prev+1] + costs[2])
                else:
                    curr_min = min(curr_min, costs[2])
            else:
                curr_min = min(curr_min, costs[2])
            # # curr_min = min(curr_min, (dp[d-1] + costs[0]) if d>0 else costs[0])
            # # curr_min = min(curr_min, (dp[d-7] + costs[1]) if d>6 else costs[1])
            # # curr_min = min(curr_min, (dp[d-30] + costs[2]) if d>29 else costs[2])
            # print(idx, dp,curr_min)
            dp[idx+1] = curr_min
        # print(dp)
        return dp[-1]
        