class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-num for num in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first, second = heapq.heappop(heap), heapq.heappop(heap)
            diff  = abs(first - second)
            if diff:
                heapq.heappush(heap, -diff)
        return -heap[0] if heap else 0
        