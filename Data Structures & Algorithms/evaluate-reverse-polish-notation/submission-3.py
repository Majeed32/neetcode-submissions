class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
                continue
            first, second = stack.pop(), stack.pop()
            if char == "+":
                stack.append(first + second)
            elif char == "-":
                stack.append(second - first)
            elif char == "*":
                stack.append(first * second)
            else:
                stack.append(int(second/first))
        return stack[-1]


        