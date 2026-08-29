class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
                continue
            if char == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(first + second)
            elif char == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif char == "*":
                first, second = stack.pop(), stack.pop()
                stack.append(first * second)
            else:
                first, second = stack.pop(), stack.pop()
                stack.append(int(second/first))
        return stack[-1]


        