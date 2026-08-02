class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # could i use a heap here?
        # we must negate for a max heap bc the python implementation is at its root a min heap
        output = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # while smaller values exist in our queue pop
                q.pop()
            q.append(r) # we are keeping track of indices in here
            # if left val out of bounds remove
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1 # we only want to increment left if the size of the window is at least k
            r += 1
        return output

        