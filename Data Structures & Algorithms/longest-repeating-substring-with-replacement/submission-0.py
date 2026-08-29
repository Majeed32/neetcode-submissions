class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = defaultdict(int)
        maxLen = left = maxFreq = 0
        for right in range(len(s)):
            myMap[s[right]] += 1
            maxFreq = max(maxFreq, myMap[s[right]])
            while (right - left + 1) - maxFreq > k:
                myMap[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen