class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sList = list(s)
        tList = list(t)
        sList.sort()
        tList.sort()
        return sList == tList
        