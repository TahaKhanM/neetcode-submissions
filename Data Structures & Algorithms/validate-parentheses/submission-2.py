from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]":"[",
            "}":"{"
        }
        stack = deque()
        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if stack[-1] == brackets[bracket]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
                
            