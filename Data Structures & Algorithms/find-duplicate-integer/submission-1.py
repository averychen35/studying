class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for val in nums:
            if val in seen:
                return val
            seen.add(val)
        return None
        