class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nums[ : k]
        heapq.heapify(arr)
        for j in range(k, len(nums)):
            heapq.heappushpop(arr, nums[j])
        return arr[0]
        