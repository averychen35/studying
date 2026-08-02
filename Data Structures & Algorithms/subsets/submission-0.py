class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # we have to do a copy so we don't modify
                return
            subset.append(nums[i])
            dfs(i+1) # include this number
            subset.pop()
            dfs(i+1) # don't include this number
        dfs(0) # keeping track of the index we're looking at
        return res