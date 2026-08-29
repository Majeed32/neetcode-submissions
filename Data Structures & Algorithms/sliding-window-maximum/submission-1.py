class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l = 0
        res = []
        for r, num in enumerate(nums):
            while queue and queue[-1] < num:
                queue.pop()
            queue.append(num)
            window_size = r-l+1
            if window_size == k:
                res.append(queue[0])
                if nums[l] == queue[0]:
                    queue.popleft()
                l += 1
        return res