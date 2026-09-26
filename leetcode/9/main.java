class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        String xString = Integer.toString(x);
        String xReverse = new StringBuilder(xString).reverse().toString();
        return xString.equals(xReverse);
    }
}
