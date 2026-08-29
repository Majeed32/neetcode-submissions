class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        n = len(s1)
        target_counter = Counter(s1)
        curr_counter = Counter(s2[ : n-1])
        l = 0
        for r in range(n-1, len(s2)):
            curr_counter[s2[r]] += 1
            if curr_counter == target_counter:
                return True
            curr_counter[s2[l]] -= 1
            if curr_counter[s2[l]] == 0:
                del curr_counter[s2[l]]
            l += 1
        return False
        