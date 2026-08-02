class Solution:
    def calculate(self, s: str) -> int:
        # call int on the value so it truncates towards 0
        # how do we ensure we do division or multiplication first
        length = len(s)
        total = 0
        operation = '+'
        stack = []

        for i in range(length):
            curr = s[i]
            if s[i].isdigit():
                total = total * 10 + int(curr)
            # final digit is added in
            if ((not curr.isdigit() and curr != " ") or i == length-1):
                if operation == '-':
                    stack.append(-total)
                elif operation == '+':
                    stack.append(total)
                elif operation == '*':
                    stack.append(stack.pop() * total)
                else:
                    stack.append(int(stack.pop()/total))
                operation = curr
                total = 0
        result = 0
        while stack:
            result += stack.pop()
        return result


        