class Solution:
    def isValid(self, s: str) -> bool:
        vals = {')' : '(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char not in vals:
                stack.append(char)
                continue
            if not stack or stack[-1] != vals[char]:
                return False
            stack.pop()
        return not stack


        