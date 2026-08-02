class Solution {
    public boolean isAnagram(String s, String t) {
        
        if (s.length() != t.length()) {
            return false;
        }
        int[] sVals = new int[26];
        int[] tVals = new int[26];
        for (int i = 0; i < s.length(); i++) {
            sVals[s.charAt(i) - 'a'] += 1;
            tVals[t.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < 26; i++) {
            if (sVals[i] != tVals[i]) {
                return false;
            }
        }
        return true;

    }
}
