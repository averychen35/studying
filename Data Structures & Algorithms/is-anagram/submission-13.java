class Solution {
    public boolean isAnagram(String s, String t) {
        int[] vals = new int[26];
        if (s.length() != t.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            vals[s.charAt(i) - 'a']++;
            vals[t.charAt(i) - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (vals[i] != 0){
                return false;
            }
        }
        return true;
        
        }
}
