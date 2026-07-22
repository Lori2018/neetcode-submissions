class Solution {
    public boolean isPalindrome(String s) {
        int i = moveIndex(-1, 1, s); 
        int j = moveIndex(s.length(), -1, s);
        while (i < s.length() && j >= 0 && i != j) {
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
                return false;
            }
            i = moveIndex(i, 1, s);
            j = moveIndex(j, -1, s);
        }
        return true;
    }

    public int moveIndex(int cur, int increment, String s) {
        String validChars = 
            "ABCDEFGHIJKLMNOPQRSTUVWYZabcdefhijklmnopqrstuvwyz1234567890";
        int x = cur + increment;
        while ((increment > 0 ? (x < s.length()) : (x >= 0)) 
                && !validChars.contains(String.valueOf(s.charAt(x)))) {
            x += increment;
        }
        return x;
    }
}
