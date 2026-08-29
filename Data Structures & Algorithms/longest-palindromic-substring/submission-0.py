class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        res = [0, 0]
        for idx, char in enumerate(s):
            odd_expand = expand(idx, idx)
            if odd_expand > res[1] - res[0]:
                distance = odd_expand//2
                res = [idx-distance, idx + distance]
            even_expand = expand(idx, idx + 1)
            if even_expand > res[1]- res[0]:
                distance = (even_expand)//2 - 1
                res = [idx-distance, idx + 1 + distance]
        i, j = res
        return s[i : j+1]

        