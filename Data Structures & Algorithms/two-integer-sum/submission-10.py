class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - value
        # keep track of the index
        index_map = {}

        for i in range(len(nums)):
            if nums[i] in index_map:
                return [index_map[nums[i]], i]
            else:
                index_map[target-nums[i]] = i
        return []
        