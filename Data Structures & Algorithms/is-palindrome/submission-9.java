class Solution {
    public boolean isPalindrome(String s) {
        String format = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int start = 0;
        int end = format.length() - 1;
        while (end > start) {
            if (format.charAt(start) != format.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
