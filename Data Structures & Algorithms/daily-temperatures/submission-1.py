class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, num in enumerate(temperatures):
            while stack and num > stack[-1][1]:
                index, n = stack.pop()
                res[index] = idx - index
            stack.append((idx, num))
        return res
        