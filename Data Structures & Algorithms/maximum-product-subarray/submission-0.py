class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxVal, minVal = 1, 1
        for n in nums:
            tmp = n * maxVal
            maxVal = max(tmp, n * minVal, n)
            minVal = min(tmp, n * minVal, n)
            res = max(maxVal, res)
        return res
        