class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                val, index = stack.pop()
                res[index] = idx - index
            stack.append((num, idx))
        return res
        