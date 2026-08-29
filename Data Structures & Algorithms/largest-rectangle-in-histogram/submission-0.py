class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for idx, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                width = idx - stack[-1][0] - 1 if stack else idx
                area = height * width
                res = max(res, area) 
            stack.append([idx, h])
        while stack:
            idx, h = stack.pop()
            width = len(heights) - stack[-1][0] - 1 if stack else len(heights)
            area = h * width
            res = max(res, area)
        return res
        