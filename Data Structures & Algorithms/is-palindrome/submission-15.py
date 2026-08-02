class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not self.isAlphaNum(s[start]):
                start += 1
            while start < end and not self.isAlphaNum(s[end]):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True




    def isAlphaNum(self, c) -> bool:
        if ord('a') <= ord(c) <= ord('z'):
            return True
        elif ord('A') <= ord(c) <= ord('Z'):
            return True
        elif ord('0') <= ord(c) <= ord('9'):
            return True
        return False

        