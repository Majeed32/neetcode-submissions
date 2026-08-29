class Solution:
    def checkValidString(self, s: str) -> bool:
        openMax, openMin = 0, 0
        for char in s:
            if char == "(":
                openMax += 1
                openMin += 1
            if char == ")":
                openMax -= 1
                openMin -= 1
            if char == "*":
                openMax += 1
                openMin -= 1
            if openMax < 0:
                return False
            openMin = max(openMin, 0)
        return openMin == 0
        