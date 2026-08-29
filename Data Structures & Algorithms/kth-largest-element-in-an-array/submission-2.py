class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [num for num in nums]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]
        