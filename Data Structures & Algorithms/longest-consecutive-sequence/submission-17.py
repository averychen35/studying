class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        curr_len = 1
        max_len = 0
        if not nums: 
            return 0
        if len(nums) == 1:
            return 1
        print(nums)
        prev_num = nums[0]
        for i in range(1, len(nums)):
            if prev_num + 1 == nums[i]:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
            elif prev_num + 1 < nums[i]:
                if curr_len > max_len:
                    max_len = curr_len
                curr_len = 1
            prev_num = nums[i]
        return max(curr_len, max_len)

        