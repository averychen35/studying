class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> vals = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            vals.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            if (vals.containsKey(target-nums[i]) && i != vals.get(target-nums[i])) {
                int[] indices = new int[2];
                indices[0] = i;
                indices[1] = vals.get(target-nums[i]);
                return indices;
            }
        }
        return null;
    }
}
