class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []
        for bracket in s:
            if bracket in my_dict:
                stack.append(bracket)
            else:
                if len(stack) == 0 or bracket != my_dict[stack.pop()]:
                    return False
        return len(stack) == 0
        