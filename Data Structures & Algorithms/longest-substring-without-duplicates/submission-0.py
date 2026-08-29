class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        my_set = set()
        left = 0
        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen

        