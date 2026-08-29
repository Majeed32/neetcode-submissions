class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for i in range(k):
            heapq.heappush(arr, nums[i])
        for j in range(k, len(nums)):
            heapq.heappushpop(arr, nums[j])
        return arr[0]
        