class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        res = []
        for right in range(len(nums)):
            while queue and nums[right] > queue[-1]:
                queue.pop()
            queue.append(nums[right])
            if right - left + 1 == k:
                res.append(queue[0])
                if nums[left] == queue[0]:
                    queue.popleft()
                left += 1
        return res
        