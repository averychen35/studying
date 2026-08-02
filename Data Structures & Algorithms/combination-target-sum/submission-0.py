class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # if we're greater, we return
        # if sum is 0, return the current combo
        # if less, then add something else
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                # remember we need to do a copy
                res.append(cur.copy())
                return
            for j in range(i, len(nums)): # because it's sorted
                # we don't want to keep going through if we're already too large
                if total + nums[j] > target:
                    return
                # this is the actual backtracking part
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        dfs(0, [], 0)
        return res