class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        first = Counter(t)
        second = defaultdict(int)
        flag = False
        left = 0
        res = [0, len(s)-1]
        count = 0
        for right in range(len(s)):
            if s[right] not in first:
                continue
            if second[s[right]] < first[s[right]]:
                count += 1
            second[s[right]] += 1
            while count == len(t):
                flag = True
                if res[1]-res[0] > right - left:
                    res = [left, right]
                second[s[left]] -= 1
                if second[s[left]] >= 0 and second[s[left]] < first[s[left]]:
                    count -= 1
                left += 1
        if not flag:
            return ""
        l, r = res
        return s[l: r+1]
        