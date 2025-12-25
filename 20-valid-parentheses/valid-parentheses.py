class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for idx, val in enumerate(s):
            if val in ['(', '{', '[']:
                stack.append(val)
                continue
            if len(stack) == 0:
                return False
            prev_val = stack.pop()
            if (val == ')' and prev_val == '(') or (val == '}' and prev_val == '{') or (val == ']' and prev_val == '['):
                continue
            
            return False

        return len(stack) == 0
             


        