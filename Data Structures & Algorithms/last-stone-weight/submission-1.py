class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-num for num in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            pop1 = -heapq.heappop(heap)
            pop2 = -heapq.heappop(heap)
            if pop1 != pop2:
                new = pop1 - pop2
                heapq.heappush(heap, -new)
        return -heap[0] if heap else 0