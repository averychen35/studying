class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = result = nums[0]

        for val in nums[1:]:
            prev_max = curr_max
            curr_max = max(val, curr_max*val, curr_min * val)
            curr_min = min(val, prev_max * val, curr_min * val)
            result = max(curr_max, result)
        return result

        