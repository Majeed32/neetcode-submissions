class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= 1:
            return arr
        l, r = 0, len(arr)-1
        while l < r:
            m = l + (r-l)//2
            if arr[m] < x:
                l = m + 1
            else:
                r = m
        first = l
        l, r = 0, len(arr)-1
        while l < r:
            m = l + (r-l+1)//2
            if arr[m] > x:
                r = m-1
            else:
                l = m
        second = l
        target = None
        if abs(arr[first] - x) < abs(arr[second] - x):
            target = first
        else:
            target = second
        l, r = target, target
        while r-l + 1 < k:
            if l == 0 or (r < len(arr) - 1 and abs(arr[r+1] - x) < abs(arr[l-1] - x)):
                r += 1
            elif r == len(arr)-1 or (l > 0 and abs(arr[l-1] - x) <= abs(arr[r+1] - x)):
                l -= 1
        return arr[l : r+1]
        