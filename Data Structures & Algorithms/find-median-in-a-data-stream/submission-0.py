class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []
        self.max_length, self.min_length = 0, 0
        

    def addNum(self, num: int) -> None:
        if not self.max_heap or num < (-self.max_heap[0]):
            heapq.heappush(self.max_heap, -num)
            self.max_length += 1
        else:
            heapq.heappush(self.min_heap, num)
            self.min_length += 1
        if self.max_length - self.min_length > 1:
            curr = -heapq.heappop(self.max_heap)
            self.max_length -= 1
            heapq.heappush(self.min_heap,curr)
            self.min_length += 1
        elif self.min_length - self.max_length > 1:
            curr = heapq.heappop(self.min_heap)
            self.min_length -= 1
            heapq.heappush(self.max_heap,-curr)
            self.max_length += 1
         

    def findMedian(self) -> float:
        if self.max_length > self.min_length:
            return -self.max_heap[0]
        elif self.max_length < self.min_length:
            return self.min_heap[0]
        return (self.min_heap[0] + (-self.max_heap[0])) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()