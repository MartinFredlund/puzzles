import java.util.Arrays;

class Solution {
    public int pivotIndex(int[] nums) {
        int pivot = 0;
        int pivotVal = nums[0];
        int leftSum = 0;
        int rightSum = Arrays.stream(nums).sum() - pivotVal;
        while(pivot < nums.length){
            if(leftSum == rightSum){
                return pivot;
            }
            leftSum += pivotVal;
            pivot ++;
            pivotVal = nums[pivot];
            rightSum -= pivotVal;
        }
        return -1;
    }
}