class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency_map = Counter(tasks)
        max_frequency = max(frequency_map.values())
        max_frequency_count = sum(1 for val in frequency_map.values() if val == max_frequency)
        cycles = (max_frequency - 1)*(n+1) + max_frequency_count
        return max(cycles, len(tasks))

        