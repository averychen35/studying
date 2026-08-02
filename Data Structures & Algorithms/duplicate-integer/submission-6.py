class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = set()
        for val in nums:
            if val not in counts:
                counts.add(val)
            else:
                return True
        return False
         