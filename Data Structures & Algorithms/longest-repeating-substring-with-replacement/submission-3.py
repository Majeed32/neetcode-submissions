class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = 0
        max_window = 0
        seen = defaultdict(int)
        for r, char in enumerate(s):
            seen[char] += 1
            max_window = max(max_window, seen[char])
            window_size = r - l + 1
            while window_size - max_window > k:
                seen[s[l]] -= 1
                window_size -= 1
                l += 1
            res = max(res, window_size)
        return res
        