class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        for i in range(1, len(nums)):
            prod[i] = nums[i-1] * prod[i-1]
        prev = 1
        for i in range(len(nums)-1, -1, -1):
            prod[i] *= prev
            prev *= nums[i]
        return prod
        