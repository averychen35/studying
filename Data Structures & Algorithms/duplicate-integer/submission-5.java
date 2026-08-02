class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
            if (counts.containsKey(val)) {
                return true;
            }
            else {
                counts.put(val, 1);
        } 
 
    }
    return false;
    }
}

