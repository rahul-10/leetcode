from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
                continue

            # if len(stack) == 0 or (char == ')' and stack[-1] != '(') or (char == '}' and stack[-1] != '{') or (char == ']' and stack[-1] != '['):
            #     return False
            
            if len(stack) > 0 and ((char == ')' and stack[-1] == '(') or (char == '}' and stack[-1] == '{') or (char == ']' and stack[-1] == '[')):
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        return False

            
            

        