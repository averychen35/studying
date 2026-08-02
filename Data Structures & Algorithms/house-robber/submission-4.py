class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_2, prev = 0, 0
        for n in nums:
            curr = max(prev_2 + n, prev)
            prev_2 = prev
            prev = curr
        return prev
        