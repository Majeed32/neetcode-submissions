class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1
            print(s[left], s[right])
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
        return True
        