class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            curr = max(n + rob1, rob2) # use the current num, or not
            rob1 = rob2
            rob2 = curr # moves rob1 and rob2 forward
        return curr

        