class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map[key]:
            return ""
        curr_list = self.time_map[key]
        l, r = 0, len(curr_list)-1
        while l < r:
            m = l + (r-l + 1)//2
            if curr_list[m][1] <= timestamp:
                l = m
            else:
                r = m - 1
        t = curr_list[l][1]
        res = curr_list[l][0]
        return res if t <= timestamp else ""
        
