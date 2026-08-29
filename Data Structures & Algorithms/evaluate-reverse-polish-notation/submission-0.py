class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+*/-":
                pop1 = stack.pop()
                pop2 = stack.pop()
                if token == "+":
                    stack.append(pop2 + pop1)
                elif token == "*":
                    stack.append(pop2*pop1)  
                elif token == "/":
                    stack.append(int(pop2/pop1))
                elif token == "-":
                    stack.append(pop2-pop1)
            else:
                stack.append(int(token))
        return stack[0]
        