package MaximumSubarray;
// 53. Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

public class MaximumSubarray {
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        System.out.println(sol.maxSubArray(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
        System.out.println(sol.maxSubArray(new int[] { 1 }));
        System.out.println(sol.maxSubArray(new int[] { 1, -2 }));
        System.out.println(sol.maxSubArray(new int[] { 5, 4, -1, 7, 8 }));
        System.out.println(sol.maxSubArray(new int[] { -1, -2, -3, -4 }));
        System.out.println(sol.maxSubArray(new int[] { -10, -2, -3, -4 }));
        
    }
}

class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int temp = 0;

        for(int i=0; i < nums.length; ++i){
            for(int j = i; j < nums.length; ++j){
                temp = 0;
                for (int k = i; k <= j; ++k) {
                    temp += nums[k];
                }
                if (temp > max){
                    max = temp;
                    System.out.println(i + ", " + j + " = " + max);
                }
            }
        }
        return max;
    }
}