import java.util.*;

class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = Arrays.stream(nums1).boxed().collect(Collectors.toSet());
        Set<Integer> set2 = Arrays.stream(nums2).boxed().collect(Collectors.toSet());

        ArrayList<Integer> uniqueSet1 = new ArrayList<>(set1);
        ArrayList<Integer> uniqueSet2 = new ArrayList<>(set2);

        uniqueSet1.removeAll(set2);
        uniqueSet2.removeAll(set1);

        return List.of(uniqueSet1, uniqueSet2);
    }
}