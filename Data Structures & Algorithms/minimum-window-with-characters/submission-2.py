class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        n = len(t)
        target = Counter(t)
        curr = Counter()
        res = ""
        curr_len = float("inf")
        l = matches = 0
        for r, char in enumerate(s):
            if char in target:
                if curr[char] < target[char]:
                    matches += 1
                curr[char] += 1
            while matches == n:
                window_size = r-l + 1
                if  window_size < curr_len:
                    res = s[l : r+1]
                    curr_len = window_size

                if s[l] in target:
                    curr[s[l]] -= 1
                    if curr[s[l]] < target[s[l]]:
                        matches -= 1
                l += 1
            
        return res
        
        