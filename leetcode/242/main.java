import java.util.HashMap;
class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> anagram = new HashMap<>();
        if(s.length() != t.length()){
            return false;
        }
        int temp_s;
        int temp_t;
        for (int i = 0; i < s.length(); i++){
            char cs = s.charAt(i);
            char ct = t.charAt(i);

            temp_s = anagram.getOrDefault(cs, 0);
            anagram.put(cs, temp_s+1);
            temp_t = anagram.getOrDefault(ct, 0);
            anagram.put(ct, temp_t-1);
        }
        for (Integer i: anagram.values()){
            if(i != 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        boolean answer = s.isAnagram("anagram","nagaram");
        System.out.println(answer);
    }
}