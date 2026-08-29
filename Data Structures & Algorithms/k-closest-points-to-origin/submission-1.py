class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(math.pow(x, 2) + math.pow(y, 2), idx) for idx, (x, y) in enumerate(points)]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            res.append(points[idx])
        return res
        
        