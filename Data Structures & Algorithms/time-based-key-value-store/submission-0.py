class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))   

    def get(self, key: str, timestamp: int) -> str:
        curr = self.map[key]
        left, right = 0, len(curr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if curr[mid][1] > timestamp:
                right = mid - 1
            elif curr[mid][1] < timestamp:
                left = mid + 1
            else:
                return curr[mid][0]
        return curr[right][0] if right >= 0 else ""