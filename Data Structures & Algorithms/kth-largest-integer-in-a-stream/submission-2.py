class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._heap = []
        self._k = k
        self._heap.extend(nums)
        heapq.heapify(self._heap)
        while len(self._heap) > k:
            heapq.heappop(self._heap)

    def add(self, val: int) -> int:
        if len(self._heap) == self._k:
            heapq.heappushpop(self._heap, val)
        else:
            heapq.heappush(self._heap, val)
        return self._heap[0]
        
