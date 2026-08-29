class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency_map = Counter(tasks)
        heap = [(-count, char) for char, count in frequency_map.items()]
        heapq.heapify(heap)
        wait_queue = deque()
        cycles = 0
        while heap or wait_queue:
            while wait_queue and wait_queue[0][0] <= cycles:
                t, freq, char = wait_queue.popleft()
                heapq.heappush(heap, (freq, char))
            if heap:
                count, char  = heapq.heappop(heap)
                count += 1
                if count < 0:
                    wait_queue.append([cycles + n + 1, count, char])
            cycles += 1
        return cycles

        