class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True) # sort in reverse order (closer to left popped first)
        stack = []
        for p, s in pair:
            stack.append((target-p)/s) # calculate the time it reaches destination
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # the two will collide, remove the one further from destination
        return len(stack)
        