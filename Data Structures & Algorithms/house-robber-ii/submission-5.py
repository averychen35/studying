class Solution:
    def house_robber(self, nums):
        prev_2, prev = 0, 0
        for n in nums:
            curr = max(prev_2 + n, prev)
            prev_2 = prev
            prev = curr
        return prev
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        max1, max2 = 0, 0
        max1 = self.house_robber(nums[0:len(nums)-1])
        max2 = self.house_robber(nums[1:])
        return max(max1, max2)
    

        