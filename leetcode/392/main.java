class Solution {
    public boolean isSubsequence(String s, String t) {
        int sTracker = 0;
        int tTracker = 0;
        while(sTracker < s.length() && tTracker < t.length()) {
            if (s.charAt(sTracker) == t.charAt(tTracker)) {
                sTracker++;
                tTracker++;
            } else {
                tTracker++;
            }
        }
        return sTracker == s.length();

    }
}