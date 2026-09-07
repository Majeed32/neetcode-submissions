class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        half = total_sum//2
        reachable = [False]*(half+1)
        reachable[0] = True

        for stone in stones:
            for i in range(half, stone-1, -1):
                if reachable[i-stone]:
                    reachable[i] = True
        max_reach = max(i for i in range(half+1) if reachable[i])
        return total_sum - 2*max_reach
        