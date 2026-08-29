class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        heap = [(-count, char) for char, count in task_counter.items()]
        heapq.heapify(heap)
        queue = deque()
        cycle = 0
        while heap or queue:
            cycle += 1
            if heap:
                count, char = heapq.heappop(heap)
                count += 1
                if count < 0:
                    queue.append((count, char, cycle + n))
            if queue and queue[0][2] == cycle:
                heapq.heappush(heap, queue.popleft()[ : 2])
        return cycle

        